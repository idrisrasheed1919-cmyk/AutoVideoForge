"""Windows setup batch file."""
@echo off
REM AutoVideoForge Setup Script for Windows

echo.
echo ========================================
echo  AutoVideoForge Setup for Windows
echo ========================================
echo.

REM Check Python
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Please install Python 3.10+
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python found!
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo Virtual environment created!
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo Virtual environment activated!
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo Dependencies installed!
echo.

REM Check FFmpeg
echo Checking FFmpeg installation...
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: FFmpeg not found
    echo Please download from: https://ffmpeg.org/download.html
    echo Then add to PATH or update FFMPEG_PATH in .env
) else (
    echo FFmpeg found!
)

echo.
echo Setup completed successfully!
echo.
echo Next steps:
echo   1. Copy .env.example to .env
echo   2. Add your API keys to .env
echo   3. Run: python main.py --topic "Your Topic"
echo.
echo For more help, see README.md
echo.
pause
