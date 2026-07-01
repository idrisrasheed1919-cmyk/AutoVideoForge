"""Time and duration utilities."""

from typing import Tuple
from datetime import timedelta

from utils.logger import get_logger

logger = get_logger(__name__)


class TimeUtils:
    """Utility functions for time/duration handling."""

    @staticmethod
    def seconds_to_time_string(seconds: float) -> str:
        """Convert seconds to HH:MM:SS format.
        
        Args:
            seconds: Duration in seconds
            
        Returns:
            Time string in HH:MM:SS format
        """
        td = timedelta(seconds=seconds)
        total_seconds = int(td.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        secs = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"

    @staticmethod
    def time_string_to_seconds(time_str: str) -> float:
        """Convert HH:MM:SS format to seconds.
        
        Args:
            time_str: Time string in HH:MM:SS or MM:SS format
            
        Returns:
            Duration in seconds
        """
        parts = time_str.split(":")
        if len(parts) == 3:
            hours, minutes, seconds = map(int, parts)
            return hours * 3600 + minutes * 60 + seconds
        elif len(parts) == 2:
            minutes, seconds = map(int, parts)
            return minutes * 60 + seconds
        else:
            return float(parts[0])

    @staticmethod
    def estimate_script_duration(script: str, wpm: int = 150) -> float:
        """Estimate script duration based on word count.
        
        Args:
            script: Script text
            wpm: Words per minute (default 150)
            
        Returns:
            Estimated duration in seconds
        """
        word_count = len(script.split())
        duration_minutes = word_count / wpm
        return duration_minutes * 60

    @staticmethod
    def get_frame_count(duration: float, fps: int) -> int:
        """Calculate frame count from duration and FPS.
        
        Args:
            duration: Duration in seconds
            fps: Frames per second
            
        Returns:
            Number of frames
        """
        return int(duration * fps)

    @staticmethod
    def get_duration_from_frames(frame_count: int, fps: int) -> float:
        """Calculate duration from frame count and FPS.
        
        Args:
            frame_count: Number of frames
            fps: Frames per second
            
        Returns:
            Duration in seconds
        """
        return frame_count / fps
