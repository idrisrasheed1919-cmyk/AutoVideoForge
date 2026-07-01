"""Configuration management utilities."""

from typing import Any, Dict, Optional
from pathlib import Path
import json

from utils.logger import get_logger

logger = get_logger(__name__)


class ConfigManager:
    """Manage application configuration."""

    def __init__(self, config_file: Optional[Path] = None):
        """Initialize config manager.
        
        Args:
            config_file: Path to config JSON file
        """
        self.config_file = config_file
        self.config: Dict[str, Any] = {}
        
        if config_file and config_file.exists():
            self.load(config_file)

    def load(self, config_file: Path) -> None:
        """Load configuration from JSON file.
        
        Args:
            config_file: Path to JSON config file
        """
        try:
            with open(config_file, "r") as f:
                self.config = json.load(f)
            logger.info(f"Configuration loaded from {config_file}")
        except Exception as e:
            logger.error(f"Failed to load configuration: {e}")
            raise

    def save(self, config_file: Path) -> None:
        """Save configuration to JSON file.
        
        Args:
            config_file: Path to save JSON config file
        """
        try:
            config_file.parent.mkdir(parents=True, exist_ok=True)
            with open(config_file, "w") as f:
                json.dump(self.config, f, indent=2)
            logger.info(f"Configuration saved to {config_file}")
        except Exception as e:
            logger.error(f"Failed to save configuration: {e}")
            raise

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set configuration value.
        
        Args:
            key: Configuration key
            value: Configuration value
        """
        self.config[key] = value

    def update(self, updates: Dict[str, Any]) -> None:
        """Update multiple configuration values.
        
        Args:
            updates: Dictionary of key-value pairs to update
        """
        self.config.update(updates)
