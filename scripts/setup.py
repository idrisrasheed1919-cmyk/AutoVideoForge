"""Automated setup script for AutoVideoForge."""

import sys
from pathlib import Path
import subprocess
import platform

from utils.logger import get_logger
from utils.file_manager import FileManager

logger = get_logger(__name__)


def check_python_version() -> bool:
    """Check if Python version is 3.10+.
    
    Returns:
        True if version is valid
    """
    if sys.version_info < (3, 10):
        logger.error(f"Python 3.10+ required, but {sys.version} found")
        return False
    logger.info(f"Python version: {sys.version}")
    return True


def check_ffmpeg() -> bool:
    """Check if FFmpeg is installed.
    
    Returns:
        True if FFmpeg is available
    """
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        logger.info("FFmpeg is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.warning("FFmpeg not found. Please install it:")
        if platform.system() == "Windows":
            logger.info("  Download from: https://ffmpeg.org/download.html")
        elif platform.system() == "Darwin":
            logger.info("  Run: brew install ffmpeg")
        else:
            logger.info("  Run: sudo apt-get install ffmpeg")
        return False


def setup_directories() -> bool:
    """Create required directories.
    
    Returns:
        True if successful
    """
    try:
        project_root = Path(__file__).parent.parent
        directories = [
            project_root / "output",
            project_root / "temp",
            project_root / "cache",
            project_root / "logs",
            project_root / "assets" / "images",
            project_root / "assets" / "music",
            project_root / "assets" / "fonts",
            project_root / "assets" / "templates",
        ]
        
        for directory in directories:
            FileManager.ensure_dir(directory)
        
        logger.info("All required directories created")
        return True
    except Exception as e:
        logger.error(f"Failed to setup directories: {e}")
        return False


def install_dependencies() -> bool:
    """Install Python dependencies.
    
    Returns:
        True if successful
    """
    try:
        logger.info("Installing Python dependencies...")
        project_root = Path(__file__).parent.parent
        requirements_file = project_root / "requirements.txt"
        
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)],
            check=True,
        )
        logger.info("Dependencies installed successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to install dependencies: {e}")
        return False


def main():
    """Run setup."""
    logger.info("Starting AutoVideoForge setup...")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check FFmpeg
    if not check_ffmpeg():
        logger.warning("Continuing without FFmpeg (required for video generation)")
    
    # Setup directories
    if not setup_directories():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    logger.info("Setup completed successfully!")
    logger.info("Next steps:")
    logger.info("  1. Copy .env.example to .env")
    logger.info("  2. Add your API keys to .env")
    logger.info("  3. Run: python main.py")


if __name__ == "__main__":
    main()
