"""Default configuration values."""

from pathlib import Path

# Directories
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"
TEMP_DIR = PROJECT_ROOT / "temp"
CACHE_DIR = PROJECT_ROOT / "cache"
LOGS_DIR = PROJECT_ROOT / "logs"
ASSETS_DIR = PROJECT_ROOT / "assets"

# Video settings
VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
VIDEO_FPS = 30
VIDEO_BITRATE = "8000k"
VIDEO_CODEC = "libx264"
AUDIO_BITRATE = "192k"
AUDIO_SAMPLE_RATE = 44100
VIDEO_PRESET = "medium"  # ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow

# Script generation
SCRIPT_MIN_LENGTH = 100
SCRIPT_MAX_LENGTH = 5000
SCRIPT_TOPIC = "technology"
SCRIPT_LANGUAGE = "english"

# Voice settings
VOICE_SPEED = 1.0
VOICE_PITCH = 1.0
VOICE_MODEL = "eleven_monolingual_v1"

# Rendering
RENDER_TIMEOUT = 3600  # seconds
MAX_PARALLEL_JOBS = 2
RENDER_QUALITY = "high"  # low, medium, high

# File paths
FFMPEG_PATH = "ffmpeg"
FFPROBE_PATH = "ffprobe"

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = LOGS_DIR / "app.log"

# API settings
API_TIMEOUT = 30
API_RETRIES = 3
API_RETRY_DELAY = 2

# Debug mode
DEBUG = False

# Validation
MIN_VIDEO_DURATION = 5  # seconds
MAX_VIDEO_DURATION = 3600  # seconds (1 hour)
