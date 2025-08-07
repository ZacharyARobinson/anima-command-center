#!/bin/bash
echo "[✓] Launching Anima..."
python3 anima.py 2>&1 | tee anima_log.txt
echo "[!] Anima exited. Log saved to anima_log.txt"
read -p "Press Enter to return to the Command Center..."
