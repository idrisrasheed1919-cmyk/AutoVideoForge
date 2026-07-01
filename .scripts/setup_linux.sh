#!/bin/bash
# AutoVideoForge Setup Script for Linux/macOS

echo ""
echo "========================================"
echo "  AutoVideoForge Setup for Linux/macOS"
echo "========================================"
echo ""

# Check Python
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 not found. Please install Python 3.10+"
    echo "Ubuntu/Debian: sudo apt-get install python3-pip"
    echo "macOS: brew install python@3.10"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "Python $PYTHON_VERSION found!"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi
echo "Virtual environment created!"
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate virtual environment"
    exit 1
fi
echo "Virtual environment activated!"
echo ""

# Upgrade pip
echo "Upgrading pip...
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "Dependencies installed!"
echo ""

# Check FFmpeg
echo "Checking FFmpeg installation..."
if ! command -v ffmpeg &> /dev/null; then
    echo "WARNING: FFmpeg not found"
    echo "Ubuntu/Debian: sudo apt-get install ffmpeg"
    echo "macOS: brew install ffmpeg"
else
    echo "FFmpeg found!"
fi

echo ""
echo "Setup completed successfully!"
echo ""
echo "Next steps:"
echo "  1. Copy .env.example to .env"
echo "  2. Add your API keys to .env"
echo "  3. Run: python main.py --topic \"Your Topic\""
echo ""
echo "For more help, see README.md"
echo ""
