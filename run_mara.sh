#!/bin/bash

# --- MARA Linux Launcher ---
# This script checks for the environment and starts MARA.

echo "=========================================="
echo "   MARA Intelligence Command Center ⚡"
echo "=========================================="

cd backend || { echo "[ERROR] Could not find backend directory."; exit 1; }

# Check for uv
if command -v uv &> /dev/null; then
    echo "[MARA] Engine: UV (Optimized)"
    USE_UV=true
else
    echo "[MARA] Engine: Python/Pip (Legacy Fallback)"
    USE_UV=false
fi

# Check for virtual environment
if [ ! -d ".venv" ]; then
    echo "[MARA] .venv not found. Initializing setup..."
    
    if $USE_UV; then
        uv venv
        uv pip install -r requirements.txt
    else
        python3 -m venv .venv
        source .venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
    fi
    
    if [ $? -ne 0 ]; then
        echo "[ERROR] Setup failed."
        exit 1
    fi
    echo "[MARA] Setup complete."
else
    echo "[MARA] Virtual environment detected."
fi

echo "[MARA] Launching Obsidian Glow UI..."
if $USE_UV; then
    uv run streamlit run app.py
else
    source .venv/bin/activate
    streamlit run app.py
fi
