"""Voice synchronization with video."""

from typing import Optional, List, Tuple
from dataclasses import dataclass

from utils.logger import get_logger
from utils.time_utils import TimeUtils

logger = get_logger(__name__)


@dataclass
class VoiceSegment:
    """Represents a voice segment with timing."""
    text: str
    start_time: float  # seconds
    end_time: float    # seconds
    duration: float    # seconds


class VoiceSynchronizer:
    """Synchronize voice with video timeline."""

    def __init__(self, total_duration: float, fps: int = 30):
        """Initialize voice synchronizer.
        
        Args:
            total_duration: Total video duration in seconds
            fps: Frames per second
        """
        self.total_duration = total_duration
        self.fps = fps
        self.segments: List[VoiceSegment] = []
        logger.info(f"Voice synchronizer initialized (duration: {total_duration}s, fps: {fps})")

    def add_segment(
        self,
        text: str,
        duration: float,
    ) -> Optional[VoiceSegment]:
        """Add voice segment to synchronization.
        
        Args:
            text: Voice segment text
            duration: Segment duration in seconds
            
        Returns:
            VoiceSegment or None if failed
        """
        if duration <= 0:
            logger.error("Segment duration must be positive")
            return None
        
        # Calculate start time based on existing segments
        start_time = sum(seg.duration for seg in self.segments)
        end_time = start_time + duration
        
        if end_time > self.total_duration:
            logger.warning(
                f"Segment exceeds total duration: {end_time}s > {self.total_duration}s"
            )
        
        segment = VoiceSegment(
            text=text,
            start_time=start_time,
            end_time=end_time,
            duration=duration,
        )
        
        self.segments.append(segment)
        logger.debug(f"Added segment: {start_time}s - {end_time}s")
        return segment

    def get_segments(self) -> List[VoiceSegment]:
        """Get all voice segments.
        
        Returns:
            List of VoiceSegment objects
        """
        return self.segments

    def get_segment_at_frame(self, frame: int) -> Optional[VoiceSegment]:
        """Get voice segment at specific frame.
        
        Args:
            frame: Frame number
            
        Returns:
            VoiceSegment or None if no segment at frame
        """
        time = frame / self.fps
        for segment in self.segments:
            if segment.start_time <= time < segment.end_time:
                return segment
        return None

    def get_frame_at_time(self, time: float) -> int:
        """Get frame number at specific time.
        
        Args:
            time: Time in seconds
            
        Returns:
            Frame number
        """
        return int(time * self.fps)

    def validate_sync(self) -> Tuple[bool, Optional[str]]:
        """Validate synchronization.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not self.segments:
            return False, "No segments added"
        
        total_duration = sum(seg.duration for seg in self.segments)
        
        if abs(total_duration - self.total_duration) > 0.5:  # 500ms tolerance
            return False, f"Total duration mismatch: {total_duration}s vs {self.total_duration}s"
        
        return True, None
