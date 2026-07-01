"""Script parsing and analysis."""

from typing import Optional, List, Tuple
import re

from utils.logger import get_logger
from utils.time_utils import TimeUtils

logger = get_logger(__name__)


class ScriptParser:
    """Parse and analyze scripts."""

    @staticmethod
    def parse_script(script: str, wpm: int = 150) -> Tuple[float, List[str]]:
        """Parse script and extract information.
        
        Args:
            script: Script text
            wpm: Words per minute for duration calculation
            
        Returns:
            Tuple of (estimated_duration_seconds, segments_list)
        """
        if not script or not isinstance(script, str):
            logger.error("Invalid script")
            return 0.0, []
        
        # Split by sentences or paragraphs
        segments = re.split(r'(?<=[.!?])\s+', script.strip())
        segments = [s.strip() for s in segments if s.strip()]
        
        # Estimate duration
        word_count = len(script.split())
        duration = (word_count / wpm) * 60  # Convert to seconds
        
        logger.info(f"Script parsed: {len(segments)} segments, {duration:.1f}s estimated duration")
        return duration, segments

    @staticmethod
    def extract_segments(script: str, segment_markers: Optional[List[str]] = None) -> List[str]:
        """Extract segments from script using markers.
        
        Args:
            script: Script text
            segment_markers: Custom segment markers (default: [SEGMENT])
            
        Returns:
            List of segments
        """
        if segment_markers is None:
            segment_markers = ["[SEGMENT]", "[PAUSE]", "[BREAK]"]
        
        segments = [script]
        
        for marker in segment_markers:
            new_segments = []
            for segment in segments:
                parts = segment.split(marker)
                new_segments.extend([p.strip() for p in parts if p.strip()])
            segments = new_segments
        
        logger.info(f"Extracted {len(segments)} segments")
        return segments

    @staticmethod
    def has_special_markers(script: str) -> bool:
        """Check if script has special markers.
        
        Args:
            script: Script text
            
        Returns:
            True if special markers found
        """
        markers = ["[PAUSE]", "[EMPHASIS]", "[SEGMENT]", "[BREAK]"]
        return any(marker in script for marker in markers)

    @staticmethod
    def remove_markers(script: str) -> str:
        """Remove special markers from script.
        
        Args:
            script: Script text
            
        Returns:
            Script without markers
        """
        markers = ["[PAUSE]", "[EMPHASIS]", "[SEGMENT]", "[BREAK]"]
        cleaned = script
        for marker in markers:
            cleaned = cleaned.replace(marker, "").replace(marker.lower(), "")
        
        # Clean up multiple spaces
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        return cleaned
