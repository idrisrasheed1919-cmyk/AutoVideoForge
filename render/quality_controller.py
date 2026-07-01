"""Video quality control."""

from typing import Optional, Dict
from pathlib import Path

from utils.logger import get_logger
from render.ffmpeg_handler import FFmpegHandler

logger = get_logger(__name__)


class QualityController:
    """Control and optimize video quality."""

    def __init__(self):
        """Initialize quality controller."""
        self.ffmpeg = FFmpegHandler()
        self.quality_presets = {
            "low": {"bitrate": "2000k", "resolution": "1280x720", "preset": "fast"},
            "medium": {"bitrate": "5000k", "resolution": "1920x1080", "preset": "medium"},
            "high": {"bitrate": "8000k", "resolution": "1920x1080", "preset": "slow"},
            "ultra": {"bitrate": "15000k", "resolution": "3840x2160", "preset": "veryslow"},
        }
        logger.info("Quality controller initialized")

    def get_preset(self, quality: str) -> Dict[str, str]:
        """Get quality preset.
        
        Args:
            quality: Quality level (low, medium, high, ultra)
            
        Returns:
            Quality preset dictionary
        """
        return self.quality_presets.get(quality, self.quality_presets["medium"])

    def validate_output(
        self,
        video_path: Path,
        min_duration: float = 1.0,
    ) -> tuple:
        """Validate generated video.
        
        Args:
            video_path: Path to video file
            min_duration: Minimum required duration
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            if not video_path.exists():
                return False, "Video file does not exist"
            
            # Check file size
            file_size = video_path.stat().st_size
            if file_size < 1000:  # Less than 1KB
                return False, "Video file too small (possibly corrupted)"
            
            # Check duration
            duration = self.ffmpeg.get_duration(video_path)
            if duration is None or duration < min_duration:
                return False, f"Video duration too short: {duration}s < {min_duration}s"
            
            logger.info(f"Video validation passed: {file_size / 1024 / 1024:.1f}MB, {duration:.1f}s")
            return True, None
        except Exception as e:
            logger.error(f"Failed to validate video: {e}")
            return False, str(e)
