# How to run Test-sangster

## Option 1: Open directly in browser (easiest)

- **Double-click** `open-app.command` in Finder, or  
- In Terminal, from this folder, run:  
  `open index.html`

The app will open in your default browser. No server needed.

---

## Option 2: Run a local server (for http://localhost:8080)

Your Mac’s built-in Python needs **Xcode Command Line Tools** before the server can run.

1. Install Command Line Tools (one-time):  
   In Terminal run:  
   `xcode-select --install`  
   Follow the prompts.

2. Start the server:  
   `cd /Users/sang/Test-sangster`  
   `python3 -m http.server 8080`

3. In your browser go to: **http://localhost:8080**

---

If you use **Node.js**, you can instead run:  
`npx serve .`  
Then open the URL it prints (often http://localhost:3000).
