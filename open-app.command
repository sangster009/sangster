#!/bin/bash
cd "$(dirname "$0")"
# Open the app in the default browser (no server needed)
open -a "Safari" "index.html" 2>/dev/null || open -a "Google Chrome" "index.html" 2>/dev/null || open "index.html"
echo "Opening Test-sangster app in your browser..."
