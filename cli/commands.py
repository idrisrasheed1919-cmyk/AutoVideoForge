"""CLI command handlers."""

from typing import Optional
import sys

from core.video_engine import VideoEngine
from config.settings import settings
from utils.logger import get_logger
from utils.validators import Validator

logger = get_logger(__name__)


class VideoCommands:
    """Handle video generation commands."""

    @staticmethod
    def generate(
        topic: str,
        duration: int = 60,
        tone: str = "informative",
        quality: str = "high",
    ) -> bool:
        """Generate video.
        
        Args:
            topic: Video topic
            duration: Target duration in seconds
            tone: Script tone
            quality: Output quality
            
        Returns:
            True if successful
        """
        # Validate inputs
        is_valid, error = Validator.validate_topic(topic)
        if not is_valid:
            logger.error(f"Invalid topic: {error}")
            return False
        
        is_valid, error = Validator.validate_duration(duration)
        if not is_valid:
            logger.error(f"Invalid duration: {error}")
            return False
        
        # Validate settings
        if not settings.validate():
            logger.error("Settings validation failed")
            return False
        
        # Generate video
        try:
            engine = VideoEngine()
            result = engine.generate_video(
                topic=topic,
                duration=duration,
                tone=tone,
                quality=quality,
            )
            
            if result:
                logger.info(f"\n🎉 Success! Video saved to: {result}")
                return True
            else:
                logger.error("\n❌ Video generation failed")
                return False
        except Exception as e:
            logger.error(f"\n❌ Error during video generation: {e}", exc_info=True)
            return False
