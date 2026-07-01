"""AI script generator."""

from typing import Optional
from pathlib import Path
from datetime import datetime

from api.gemini_client import GeminiClient
from api.openai_client import OpenAIClient
from config.settings import settings
from utils.logger import get_logger
from utils.file_manager import FileManager
from utils.time_utils import TimeUtils
from utils.validators import Validator

logger = get_logger(__name__)


class ScriptGenerator:
    """Generate video scripts using AI."""

    def __init__(self, use_openai: bool = False):
        """Initialize script generator.
        
        Args:
            use_openai: Use OpenAI instead of Gemini
        """
        if use_openai and settings.openai_api_key:
            self.client = OpenAIClient(settings.openai_api_key)
            self.provider = "OpenAI"
        elif settings.gemini_api_key:
            self.client = GeminiClient(settings.gemini_api_key)
            self.provider = "Gemini"
        else:
            raise ValueError("No API key configured for script generation")
        
        logger.info(f"Script generator initialized with {self.provider}")

    def generate(
        self,
        topic: str,
        duration: int = 60,
        tone: str = "informative",
        save_to_file: bool = True,
    ) -> Optional[str]:
        """Generate video script.
        
        Args:
            topic: Video topic
            duration: Target duration in seconds
            tone: Script tone (informative, entertaining, educational, etc.)
            save_to_file: Save script to file
            
        Returns:
            Generated script or None if failed
        """
        # Validate inputs
        is_valid, error = Validator.validate_topic(topic)
        if not is_valid:
            logger.error(f"Invalid topic: {error}")
            return None
        
        is_valid, error = Validator.validate_duration(duration)
        if not is_valid:
            logger.error(f"Invalid duration: {error}")
            return None
        
        logger.info(f"Generating script - Topic: {topic}, Duration: {duration}s, Tone: {tone}")
        
        # Generate script
        script = self.client.generate_script(
            topic=topic,
            duration=duration,
            tone=tone,
            language="english",
        )
        
        if not script:
            logger.error("Failed to generate script")
            return None
        
        # Save to file if requested
        if save_to_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            script_path = settings.output_dir / f"script_{timestamp}.txt"
            
            try:
                script_path.parent.mkdir(parents=True, exist_ok=True)
                script_path.write_text(script, encoding="utf-8")
                logger.info(f"Script saved to {script_path}")
            except Exception as e:
                logger.error(f"Failed to save script: {e}")
        
        return script

    def refine(self, script: str, feedback: str) -> Optional[str]:
        """Refine existing script.
        
        Args:
            script: Original script
            feedback: Refinement feedback
            
        Returns:
            Refined script or None if failed
        """
        logger.info("Refining script based on feedback")
        
        refined_script = self.client.refine_script(script, feedback)
        
        if not refined_script:
            logger.error("Failed to refine script")
            return None
        
        return refined_script
