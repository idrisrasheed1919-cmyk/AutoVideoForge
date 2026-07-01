"""Logging setup and utilities."""

import logging
import sys
from pathlib import Path
from typing import Optional

from config.env_loader import EnvLoader
from config import defaults

# Color codes for terminal output
COLORS = {
    "DEBUG": "\033[36m",      # Cyan
    "INFO": "\033[32m",       # Green
    "WARNING": "\033[33m",    # Yellow
    "ERROR": "\033[31m",      # Red
    "CRITICAL": "\033[35m",   # Magenta
    "RESET": "\033[0m",       # Reset
}


class ColoredFormatter(logging.Formatter):
    """Formatter that adds colors to log output."""

    def format(self, record):
        """Format log record with colors.
        
        Args:
            record: Log record
            
        Returns:
            Formatted log string
        """
        log_color = COLORS.get(record.levelname, COLORS["RESET"])
        record.levelname = f"{log_color}{record.levelname}{COLORS['RESET']}"
        return super().format(record)


def setup_logging(
    name: Optional[str] = None,
    level: Optional[str] = None,
    log_file: Optional[Path] = None,
) -> logging.Logger:
    """Setup logging configuration.
    
    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional file path for log output
        
    Returns:
        Configured logger instance
    """
    if name is None:
        name = __name__
    
    # Get log level from environment or use default
    env = EnvLoader()
    if level is None:
        level = env.get("LOG_LEVEL", defaults.LOG_LEVEL)
    
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    
    # Remove existing handlers
    logger.handlers.clear()
    
    # Console handler with colors
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, level.upper(), logging.INFO))
    console_formatter = ColoredFormatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # File handler
    if log_file is None:
        log_file = defaults.LOG_FILE
    
    log_file.parent.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(getattr(logging, level.upper(), logging.INFO))
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    return logger


def get_logger(name: str) -> logging.Logger:
    """Get or create a logger.
    
    Args:
        name: Logger name (usually __name__)
        
    Returns:
        Logger instance
    """
    return setup_logging(name)
