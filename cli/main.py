"""Main CLI entry point."""

import sys
from typing import Optional
import click

from cli.commands import VideoCommands
from cli.validators import CLIValidator
from utils.logger import get_logger, setup_logging

logger = get_logger(__name__)


@click.group()
@click.option("--debug", is_flag=True, help="Enable debug logging")
def app(debug):
    """AutoVideoForge - AI Video Automation System."""
    if debug:
        setup_logging(level="DEBUG")
        logger.info("Debug mode enabled")


@app.command()
@click.option(
    "--topic",
    required=True,
    help="Video topic",
    type=str,
)
@click.option(
    "--duration",
    default=60,
    help="Video duration in seconds",
    type=int,
)
@click.option(
    "--tone",
    default="informative",
    help="Script tone (informative, entertaining, educational, etc.)",
    type=str,
)
@click.option(
    "--quality",
    default="high",
    help="Output quality (low, medium, high, ultra)",
    type=str,
)
def generate(topic: str, duration: int, tone: str, quality: str):
    """Generate AI video."""
    # Validate tone
    is_valid, error = CLIValidator.validate_tone(tone)
    if not is_valid:
        logger.error(f"Invalid tone: {error}")
        sys.exit(1)
    
    # Validate quality
    is_valid, error = CLIValidator.validate_quality(quality)
    if not is_valid:
        logger.error(f"Invalid quality: {error}")
        sys.exit(1)
    
    # Generate video
    success = VideoCommands.generate(
        topic=topic,
        duration=duration,
        tone=tone,
        quality=quality,
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    app()
