"""OpenAI API client for script generation."""

from typing import Optional
import openai

from utils.logger import get_logger
from utils.validators import Validator

logger = get_logger(__name__)


class OpenAIClient:
    """Client for OpenAI API."""

    def __init__(self, api_key: str):
        """Initialize OpenAI client.
        
        Args:
            api_key: OpenAI API key
        """
        is_valid, error = Validator.validate_api_key(api_key)
        if not is_valid:
            raise ValueError(f"Invalid API key: {error}")
        
        openai.api_key = api_key
        self.model = "gpt-3.5-turbo"
        logger.info("OpenAI client initialized")

    def generate_script(
        self,
        topic: str,
        duration: int = 60,
        tone: str = "informative",
        language: str = "english",
    ) -> Optional[str]:
        """Generate video script using OpenAI.
        
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
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=2000,
            )
            script = response.choices[0].message.content.strip()
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
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=2000,
            )
            refined_script = response.choices[0].message.content.strip()
            logger.info("Script refined successfully")
            return refined_script
        except Exception as e:
            logger.error(f"Failed to refine script: {e}")
            return None
