"""Installation guide."""

# Installation Guide

## System Requirements

- Python 3.10 or higher
- FFmpeg (optional but recommended)
- 4GB RAM minimum
- 10GB free disk space

## Quick Installation

### Windows

1. Install Python from https://www.python.org/downloads/
2. Clone the repository:
   ```bash
   git clone https://github.com/idrisrasheed1919-cmyk/AutoVideoForge.git
   cd AutoVideoForge
   ```
3. Run setup script:
   ```bash
   .scripts\setup_windows.bat
   ```

### Linux/macOS

1. Clone the repository:
   ```bash
   git clone https://github.com/idrisrasheed1919-cmyk/AutoVideoForge.git
   cd AutoVideoForge
   ```
2. Run setup script:
   ```bash
   chmod +x .scripts/setup_linux.sh
   ./.scripts/setup_linux.sh
   ```

## Manual Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## FFmpeg Installation

### Windows
- Download from https://ffmpeg.org/download.html
- Add to PATH or set FFMPEG_PATH in .env

### Ubuntu/Debian
```bash
sudo apt-get install ffmpeg
```

### macOS
```bash
brew install ffmpeg
```

## Verify Installation

```bash
python -m pytest tests/ -v
```
