"""Input validation utilities."""

from typing import Optional, Tuple
import re

from utils.logger import get_logger

logger = get_logger(__name__)


class Validator:
    """Validate input data."""

    @staticmethod
    def validate_topic(topic: str) -> Tuple[bool, Optional[str]]:
        """Validate video topic.
        
        Args:
            topic: Topic string
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not topic or not isinstance(topic, str):
            return False, "Topic must be a non-empty string"
        
        if len(topic) < 3:
            return False, "Topic must be at least 3 characters long"
        
        if len(topic) > 200:
            return False, "Topic must be less than 200 characters"
        
        # Check for invalid characters
        if not re.match(r"^[a-zA-Z0-9\s\-_,'\.]+$", topic):
            return False, "Topic contains invalid characters"
        
        return True, None

    @staticmethod
    def validate_duration(duration: int, min_duration: int = 5, max_duration: int = 3600) -> Tuple[bool, Optional[str]]:
        """Validate video duration.
        
        Args:
            duration: Duration in seconds
            min_duration: Minimum duration
            max_duration: Maximum duration
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(duration, int):
            return False, "Duration must be an integer"
        
        if duration < min_duration:
            return False, f"Duration must be at least {min_duration} seconds"
        
        if duration > max_duration:
            return False, f"Duration must be less than {max_duration} seconds"
        
        return True, None

    @staticmethod
    def validate_api_key(api_key: str) -> Tuple[bool, Optional[str]]:
        """Validate API key format.
        
        Args:
            api_key: API key string
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not api_key or not isinstance(api_key, str):
            return False, "API key must be a non-empty string"
        
        if len(api_key) < 10:
            return False, "API key appears to be too short"
        
        return True, None

    @staticmethod
    def validate_email(email: str) -> Tuple[bool, Optional[str]]:
        """Validate email format.
        
        Args:
            email: Email string
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return True, None
        return False, "Invalid email format"
