"""Timeline management for video."""

from typing import List, Optional
from dataclasses import dataclass

from utils.logger import get_logger

logger = get_logger(__name__)


@dataclass
class TimelineEvent:
    """Represents an event on the timeline."""
    name: str
    start_time: float  # seconds
    duration: float    # seconds
    data: dict = None  # Additional event data

    @property
    def end_time(self) -> float:
        """Get end time of event."""
        return self.start_time + self.duration


class Timeline:
    """Manage video timeline and events."""

    def __init__(self, total_duration: float):
        """Initialize timeline.
        
        Args:
            total_duration: Total timeline duration in seconds
        """
        self.total_duration = total_duration
        self.events: List[TimelineEvent] = []
        logger.info(f"Timeline initialized: {total_duration}s")

    def add_event(
        self,
        name: str,
        start_time: float,
        duration: float,
        data: dict = None,
    ) -> Optional[TimelineEvent]:
        """Add event to timeline.
        
        Args:
            name: Event name
            start_time: Start time in seconds
            duration: Duration in seconds
            data: Optional event data
            
        Returns:
            TimelineEvent or None if failed
        """
        if start_time < 0 or start_time + duration > self.total_duration:
            logger.error(f"Event exceeds timeline bounds: {start_time}s + {duration}s")
            return None
        
        event = TimelineEvent(
            name=name,
            start_time=start_time,
            duration=duration,
            data=data or {},
        )
        
        self.events.append(event)
        self.events.sort(key=lambda e: e.start_time)
        logger.debug(f"Event added: {name} @ {start_time}s ({duration}s)")
        return event

    def get_events_at_time(self, time: float) -> List[TimelineEvent]:
        """Get all events at specific time.
        
        Args:
            time: Time in seconds
            
        Returns:
            List of TimelineEvent objects
        """
        return [e for e in self.events if e.start_time <= time < e.end_time]

    def get_events(self) -> List[TimelineEvent]:
        """Get all events.
        
        Returns:
            List of TimelineEvent objects
        """
        return self.events

    def clear_events(self) -> None:
        """Clear all events."""
        self.events.clear()
        logger.debug("Timeline cleared")
