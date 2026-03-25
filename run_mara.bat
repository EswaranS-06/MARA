@echo off
SETLOCAL EnableDelayedExpansion

:: --- MARA Windows Launcher ---
:: This script checks for the environment and starts MARA.

echo ==========================================
echo    MARA Intelligence Command Center ⚡
echo ==========================================

cd backend

:: Check if uv is installed
where uv >nul 2>nul
if %ERRORLEVEL% equ 0 (
    @echo [MARA] Engine: UV (Optimized)
    set "USE_UV=1"
) else (
    @echo [MARA] Engine: Python/Pip (Legacy Fallback)
    set "USE_UV=0"
)

:: Check for virtual environment
if not exist ".venv" (
    echo [MARA] .venv not found. Initializing setup...
    
    if "%USE_UV%"=="1" (
        uv venv
        if !ERRORLEVEL! neq 0 ( exit /b 1 )
        echo [MARA] Installing dependencies via uv...
        uv pip install -r requirements.txt
    ) else (
        python -m venv .venv
        if !ERRORLEVEL! neq 0 ( 
            echo [ERROR] Could not create venv. Is Python installed?
            pause
            exit /b 1 
        )
        echo [MARA] Installing dependencies via pip...
        call .venv\Scripts\activate
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    )
    
    if !ERRORLEVEL! neq 0 (
        echo [ERROR] Setup failed.
        pause
        exit /b 1
    )
    echo [MARA] Setup complete.
) else (
    echo [MARA] Virtual environment detected.
)

echo [MARA] Launching Obsidian Glow UI...
if "%USE_UV%"=="1" (
    uv run streamlit run app.py
) else (
    call .venv\Scripts\activate
    streamlit run app.py
)
pause
