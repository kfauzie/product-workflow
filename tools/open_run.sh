#!/bin/bash
# Open a run's prototype in the browser, from any folder inside the repo.
# Usage: tools/open_run.sh                       (the fictional example: examples/relaywise/run)
#        tools/open_run.sh path/to/run           (any run folder with build/mvp.html)
set -e
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "Run this from inside the repo folder."; exit 1; }
DIR="${1:-examples/relaywise/run}"
case "$DIR" in /*) ;; *) DIR="$ROOT/$DIR" ;; esac
[ -f "$DIR/build/mvp.html" ] || { echo "No prototype at $DIR/build/mvp.html"; exit 1; }
PORT=8000; while lsof -i :$PORT >/dev/null 2>&1; do PORT=$((PORT+1)); done   # first free port
URL="http://localhost:$PORT/build/mvp.html"
echo "Prototype: $URL   (Control+C to stop)"
( sleep 1; open "$URL" 2>/dev/null || xdg-open "$URL" 2>/dev/null ) &
cd "$DIR" && exec python3 -m http.server $PORT
