#!/usr/bin/env python3
"""
Instrumented launcher to debug why http://localhost:8080/ may not be reachable.
"""
import socket
import sys
import os
import json
import threading
import subprocess

LOG_PATH = "/Users/sang/sangster/.cursor/debug-635809.log"
SESSION_ID = "635809"
PORT = 8080
PROJECT_DIR = "/Users/sang/sangster"

def log(location, message, data=None, hypothesis_id=None):
    # #region agent log
    payload = {
        "sessionId": SESSION_ID,
        "id": f"log_{location.replace(':', '_')}",
        "timestamp": int(__import__("time").time() * 1000),
        "location": f"run_server.py:{location}",
        "message": message,
        "data": data or {},
    }
    if hypothesis_id:
        payload["hypothesisId"] = hypothesis_id
    try:
        with open(LOG_PATH, "a") as f:
            f.write(json.dumps(payload) + "\n")
    except Exception:
        pass
    # #endregion

def port_in_use(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", port))
            return False
    except OSError:
        return True

def free_port(port):
    """Try to free the given port by killing processes listening on it (macOS/Linux)."""
    try:
        out = subprocess.run(
            ["lsof", "-ti", f":{port}"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if out.returncode != 0 or not out.stdout.strip():
            return []
        pids = [p.strip() for p in out.stdout.strip().split() if p.strip()]
        for pid in pids:
            subprocess.run(["kill", pid], capture_output=True, timeout=2)
        return pids
    except Exception as e:
        return []

def main():
    # H1: port 8080 in use?
    in_use = port_in_use(PORT)
    log("port_check", "Port 8080 availability", {"port": PORT, "in_use": in_use}, "H1")

    # H3: cwd
    cwd = os.getcwd()
    log("cwd", "Current working directory", {"cwd": cwd, "expected": PROJECT_DIR}, "H3")

    os.chdir(PROJECT_DIR)

    # H1 fix: if port in use, free it then recheck
    if in_use:
        pids = free_port(PORT)
        log("port_freed", "Freed port 8080", {"killed_pids": pids}, "H1")
        import time
        time.sleep(0.3)
        in_use = port_in_use(PORT)
        log("port_check_after_free", "Port 8080 after free", {"port": PORT, "in_use": in_use}, "H1")
        if in_use:
            log("abort", "Not starting server (port still in use)", {}, "H1")
            print("Port 8080 is still in use after freeing. Check with: lsof -i :8080", file=sys.stderr)
            sys.exit(1)

    server_error = [None]  # use list so inner function can set

    def run_http_server():
        try:
            import http.server
            import socketserver
            handler = http.server.SimpleHTTPRequestHandler
            httpd = socketserver.TCPServer(("", PORT), handler)
            log("bind", "Server bound", {"address": list(httpd.server_address), "port": PORT}, "H4")
            log("serving", "Serving HTTP", {"port": PORT}, "H5")
            try:
                httpd.serve_forever()
            finally:
                httpd.server_close()
        except Exception as e:
            server_error[0] = e
            log("server_error", "Server exception", {"error": str(e), "type": type(e).__name__}, "H2")

    t = threading.Thread(target=run_http_server, daemon=True)
    t.start()
    # Give server time to bind
    import time
    time.sleep(0.5)
    if server_error[0]:
        log("start_failed", "Server thread raised", {"error": str(server_error[0])}, "H2")
        sys.exit(1)
    log("ready", "Server thread started; ready for connections", {"port": PORT}, "H5")
    print(f"Serving at http://localhost:{PORT}/  (Ctrl+C to stop)")
    try:
        t.join()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
