"""Global settings manager."""

from typing import Optional
from pathlib import Path

from config.env_loader import EnvLoader
from config import defaults
from utils.logger import get_logger

logger = get_logger(__name__)


class Settings:
    """Centralized settings management."""

    def __init__(self):
        """Initialize settings from environment and defaults."""
        self.env = EnvLoader()
        
        # Directories
        self.output_dir = self._get_path("OUTPUT_DIR", defaults.OUTPUT_DIR)
        self.temp_dir = self._get_path("TEMP_DIR", defaults.TEMP_DIR)
        self.cache_dir = self._get_path("CACHE_DIR", defaults.CACHE_DIR)
        self.logs_dir = self._get_path("LOGS_DIR", defaults.LOGS_DIR)
        
        # Create directories
        for directory in [self.output_dir, self.temp_dir, self.cache_dir, self.logs_dir]:
            directory.mkdir(parents=True, exist_ok=True)
        
        # Video settings
        self.video_width = self.env.get_int("VIDEO_WIDTH", defaults.VIDEO_WIDTH)
        self.video_height = self.env.get_int("VIDEO_HEIGHT", defaults.VIDEO_HEIGHT)
        self.video_fps = self.env.get_int("VIDEO_FPS", defaults.VIDEO_FPS)
        self.video_bitrate = self.env.get("VIDEO_BITRATE", defaults.VIDEO_BITRATE)
        self.video_codec = self.env.get("VIDEO_CODEC", defaults.VIDEO_CODEC)
        self.audio_bitrate = self.env.get("AUDIO_BITRATE", defaults.AUDIO_BITRATE)
        self.audio_sample_rate = self.env.get_int("AUDIO_SAMPLE_RATE", defaults.AUDIO_SAMPLE_RATE)
        
        # Script settings
        self.script_min_length = self.env.get_int("SCRIPT_MIN_LENGTH", defaults.SCRIPT_MIN_LENGTH)
        self.script_max_length = self.env.get_int("SCRIPT_MAX_LENGTH", defaults.SCRIPT_MAX_LENGTH)
        self.script_topic = self.env.get("SCRIPT_TOPIC", defaults.SCRIPT_TOPIC)
        
        # Voice settings
        self.voice_speed = self.env.get_float("VOICE_SPEED", defaults.VOICE_SPEED)
        self.voice_pitch = self.env.get_float("VOICE_PITCH", defaults.VOICE_PITCH)
        
        # Rendering
        self.render_timeout = self.env.get_int("RENDER_TIMEOUT", defaults.RENDER_TIMEOUT)
        self.max_parallel_jobs = self.env.get_int("MAX_PARALLEL_JOBS", defaults.MAX_PARALLEL_JOBS)
        
        # File paths
        self.ffmpeg_path = self.env.get("FFMPEG_PATH", defaults.FFMPEG_PATH)
        self.ffprobe_path = self.env.get("FFPROBE_PATH", defaults.FFPROBE_PATH)
        
        # API keys
        self.gemini_api_key = self.env.get("GEMINI_API_KEY")
        self.openai_api_key = self.env.get("OPENAI_API_KEY")
        self.elevenlabs_api_key = self.env.get("ELEVENLABS_API_KEY")
        self.elevenlabs_voice_id = self.env.get("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM")
        
        # Logging
        self.log_level = self.env.get("LOG_LEVEL", defaults.LOG_LEVEL)
        self.debug = self.env.get_bool("DEBUG", defaults.DEBUG)
        
        logger.info("Settings loaded successfully")

    @staticmethod
    def _get_path(env_key: str, default: Path) -> Path:
        """Get path from environment or use default.
        
        Args:
            env_key: Environment variable key
            default: Default path
            
        Returns:
            Path object
        """
        value = EnvLoader.get(env_key)
        if value:
            return Path(value).expanduser().resolve()
        return default

    def validate(self) -> bool:
        """Validate critical settings.
        
        Returns:
            True if valid, False otherwise
        """
        errors = []
        
        # Check API keys
        if not self.gemini_api_key and not self.openai_api_key:
            errors.append("GEMINI_API_KEY or OPENAI_API_KEY must be set")
        
        if not self.elevenlabs_api_key:
            errors.append("ELEVENLABS_API_KEY must be set")
        
        # Check video dimensions
        if self.video_width < 640 or self.video_height < 480:
            errors.append("Video dimensions too small (minimum 640x480)")
        
        if self.video_width > 4096 or self.video_height > 4096:
            errors.append("Video dimensions too large (maximum 4096x4096)")
        
        # Check FPS
        if self.video_fps < 1 or self.video_fps > 120:
            errors.append("Video FPS must be between 1 and 120")
        
        if errors:
            for error in errors:
                logger.error(f"Settings validation error: {error}")
            return False
        
        return True


# Global settings instance
settings = Settings()
