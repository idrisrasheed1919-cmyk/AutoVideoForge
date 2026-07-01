"""Environment variable loader."""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


class EnvLoader:
    """Load and manage environment variables."""

    def __init__(self, env_file: Optional[str] = None):
        """Initialize environment loader.
        
        Args:
            env_file: Path to .env file (defaults to .env in project root)
        """
        if env_file is None:
            env_file = Path(__file__).parent.parent / ".env"
        
        self.env_file = Path(env_file)
        if self.env_file.exists():
            load_dotenv(self.env_file)

    @staticmethod
    def get(key: str, default: Optional[str] = None) -> Optional[str]:
        """Get environment variable.
        
        Args:
            key: Environment variable name
            default: Default value if not found
            
        Returns:
            Environment variable value or default
        """
        return os.getenv(key, default)

    @staticmethod
    def get_int(key: str, default: int = 0) -> int:
        """Get integer environment variable.
        
        Args:
            key: Environment variable name
            default: Default value if not found
            
        Returns:
            Integer value or default
        """
        value = os.getenv(key)
        if value is None:
            return default
        try:
            return int(value)
        except ValueError:
            return default

    @staticmethod
    def get_bool(key: str, default: bool = False) -> bool:
        """Get boolean environment variable.
        
        Args:
            key: Environment variable name
            default: Default value if not found
            
        Returns:
            Boolean value or default
        """
        value = os.getenv(key, "false").lower()
        if value in ("true", "1", "yes", "on"):
            return True
        if value in ("false", "0", "no", "off"):
            return False
        return default

    @staticmethod
    def get_float(key: str, default: float = 0.0) -> float:
        """Get float environment variable.
        
        Args:
            key: Environment variable name
            default: Default value if not found
            
        Returns:
            Float value or default
        """
        value = os.getenv(key)
        if value is None:
            return default
        try:
            return float(value)
        except ValueError:
            return default
