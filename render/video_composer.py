"""Video composition and assembly."""

from typing import Optional, List
from pathlib import Path
from pydub import AudioSegment
from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
    ImageClip,
    TextClip,
    concatenate_videoclips,
    CompositeVideoClip,
)
import numpy as np

from utils.logger import get_logger
from config.settings import settings
from render.ffmpeg_handler import FFmpegHandler

logger = get_logger(__name__)


class VideoComposer:
    """Compose and assemble videos."""

    def __init__(self):
        """Initialize video composer."""
        self.ffmpeg = FFmpegHandler()
        logger.info("Video composer initialized")

    def create_blank_video(
        self,
        duration: float,
        width: int,
        height: int,
        fps: int,
        color: tuple = (0, 0, 0),
    ) -> Optional[VideoFileClip]:
        """Create blank video clip.
        
        Args:
            duration: Duration in seconds
            width: Video width
            height: Video height
            fps: Frames per second
            color: RGB color tuple
            
        Returns:
            VideoFileClip or None if failed
        """
        try:
            logger.info(f"Creating blank video: {width}x{height} @ {fps}fps for {duration}s")
            
            def make_frame(t):
                return np.zeros((height, width, 3), dtype=np.uint8)
            
            clip = VideoClip(make_frame, duration=duration)
            clip = clip.set_fps(fps)
            logger.debug("Blank video created")
            return clip
        except Exception as e:
            logger.error(f"Failed to create blank video: {e}")
            return None

    def add_audio_to_video(
        self,
        video_path: Path,
        audio_path: Path,
        output_path: Path,
    ) -> bool:
        """Add audio to video.
        
        Args:
            video_path: Path to video file
            audio_path: Path to audio file
            output_path: Output video path
            
        Returns:
            True if successful
        """
        try:
            logger.info("Adding audio to video...")
            
            video = VideoFileClip(str(video_path))
            audio = AudioFileClip(str(audio_path))
            
            # Get minimum duration
            min_duration = min(video.duration, audio.duration)
            video = video.subclipped(0, min_duration)
            audio = audio.subclipped(0, min_duration)
            
            video = video.set_audio(audio)
            video.write_videofile(
                str(output_path),
                codec=settings.video_codec,
                audio_codec="aac",
                fps=settings.video_fps,
                verbose=False,
                logger=None,
            )
            
            video.close()
            audio.close()
            logger.info(f"Video with audio saved: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to add audio to video: {e}")
            return False

    def generate_thumbnail(
        self,
        video_path: Path,
        output_path: Path,
        timestamp: float = 5.0,
    ) -> bool:
        """Generate thumbnail from video.
        
        Args:
            video_path: Path to video file
            output_path: Output image path
            timestamp: Timestamp to extract (seconds)
            
        Returns:
            True if successful
        """
        try:
            logger.info(f"Generating thumbnail at {timestamp}s...")
            return self.ffmpeg.extract_frame(video_path, output_path, timestamp)
        except Exception as e:
            logger.error(f"Failed to generate thumbnail: {e}")
            return False
