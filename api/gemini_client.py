"""Gemini API client for script generation."""

from typing import Optional
import google.generativeai as genai

from utils.logger import get_logger
from utils.validators import Validator

logger = get_logger(__name__)


class GeminiClient:
    """Client for Google Gemini API."""

    def __init__(self, api_key: str):
        """Initialize Gemini client.
        
        Args:
            api_key: Gemini API key
        """
        is_valid, error = Validator.validate_api_key(api_key)
        if not is_valid:
            raise ValueError(f"Invalid API key: {error}")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")
        logger.info("Gemini client initialized")

    def generate_script(
        self,
        topic: str,
        duration: int = 60,
        tone: str = "informative",
        language: str = "english",
    ) -> Optional[str]:
        """Generate video script using Gemini.
        
        Args:
            topic: Video topic
            duration: Target duration in seconds (estimate for word count)
            tone: Tone of script (informative, entertaining, educational, etc.)
            language: Language for script
            
        Returns:
            Generated script or None if failed
        """
        is_valid, error = Validator.validate_topic(topic)
        if not is_valid:
            logger.error(f"Invalid topic: {error}")
            return None
        
        # Estimate word count (150 words per minute = 2.5 words per second)
        estimated_words = int(duration * 2.5)
        
        prompt = f"""
Generate a compelling {tone} video script about "{topic}" in {language}.

Requirements:
- Target length: approximately {estimated_words} words
- Professional and engaging tone
- Clear introduction, body, and conclusion
- Include natural pauses (marked with [PAUSE])
- Add emphasis markers for important points [EMPHASIS]
- Keep sentences concise and conversational
- No markdown formatting, plain text only

Script:
"""
        
        try:
            logger.info(f"Generating script for topic: {topic}")
            response = self.model.generate_content(prompt)
            script = response.text.strip()
            logger.info(f"Script generated successfully ({len(script)} characters)")
            return script
        except Exception as e:
            logger.error(f"Failed to generate script: {e}")
            return None

    def refine_script(self, script: str, feedback: str) -> Optional[str]:
        """Refine generated script based on feedback.
        
        Args:
            script: Original script
            feedback: Feedback for refinement
            
        Returns:
            Refined script or None if failed
        """
        prompt = f"""
Please refine the following script based on this feedback: {feedback}

Original Script:
{script}

Refined Script:
"""
        
        try:
            logger.info("Refining script based on feedback")
            response = self.model.generate_content(prompt)
            refined_script = response.text.strip()
            logger.info("Script refined successfully")
            return refined_script
        except Exception as e:
            logger.error(f"Failed to refine script: {e}")
            return None
