"""CLI validators."""

from typing import Tuple, Optional

from utils.validators import Validator as BaseValidator


class CLIValidator:
    """CLI-specific validators."""

    @staticmethod
    def validate_quality(quality: str) -> Tuple[bool, Optional[str]]:
        """Validate quality setting.
        
        Args:
            quality: Quality level
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        valid_qualities = ["low", "medium", "high", "ultra"]
        
        if quality not in valid_qualities:
            return False, f"Quality must be one of: {', '.join(valid_qualities)}"
        
        return True, None

    @staticmethod
    def validate_tone(tone: str) -> Tuple[bool, Optional[str]]:
        """Validate tone setting.
        
        Args:
            tone: Script tone
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        valid_tones = [
            "informative",
            "entertaining",
            "educational",
            "formal",
            "casual",
            "professional",
        ]
        
        if tone not in valid_tones:
            return False, f"Tone must be one of: {', '.join(valid_tones)}"
        
        return True, None
