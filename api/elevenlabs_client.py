"""ElevenLabs API client for voice synthesis."""

from typing import Optional
from pathlib import Path
import requests

from utils.logger import get_logger
from utils.validators import Validator

logger = get_logger(__name__)

ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1"


class ElevenLabsClient:
    """Client for ElevenLabs API."""

    def __init__(self, api_key: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM"):
        """Initialize ElevenLabs client.
        
        Args:
            api_key: ElevenLabs API key
            voice_id: Voice ID to use for TTS
        """
        is_valid, error = Validator.validate_api_key(api_key)
        if not is_valid:
            raise ValueError(f"Invalid API key: {error}")
        
        self.api_key = api_key
        self.voice_id = voice_id
        self.headers = {"xi-api-key": api_key}
        logger.info(f"ElevenLabs client initialized with voice_id: {voice_id}")

    def text_to_speech(
        self,
        text: str,
        output_path: Path,
        model_id: str = "eleven_monolingual_v1",
        stability: float = 0.5,
        clarity_boost: bool = True,
    ) -> bool:
        """Convert text to speech.
        
        Args:
            text: Text to convert
            output_path: Path to save audio file
            model_id: Model ID for TTS
            stability: Stability parameter (0-1)
            clarity_boost: Enable clarity boost
            
        Returns:
            True if successful, False otherwise
        """
        if not text or not isinstance(text, str):
            logger.error("Text must be a non-empty string")
            return False
        
        url = f"{ELEVENLABS_API_URL}/text-to-speech/{self.voice_id}"
        
        payload = {
            "text": text,
            "model_id": model_id,
            "voice_settings": {
                "stability": stability,
                "similarity_boost": 0.75,
            },
        }
        
        try:
            logger.info(f"Converting text to speech ({len(text)} characters)")
            response = requests.post(url, json=payload, headers=self.headers, timeout=60)
            
            if response.status_code != 200:
                logger.error(f"API error: {response.status_code} - {response.text}")
                return False
            
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(response.content)
            
            logger.info(f"Audio saved to {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to generate speech: {e}")
            return False

    def get_voices(self) -> Optional[list]:
        """Get available voices.
        
        Returns:
            List of available voices or None if failed
        """
        url = f"{ELEVENLABS_API_URL}/voices"
        
        try:
            logger.info("Fetching available voices")
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                logger.error(f"API error: {response.status_code}")
                return None
            
            voices = response.json().get("voices", [])
            logger.info(f"Retrieved {len(voices)} voices")
            return voices
        except Exception as e:
            logger.error(f"Failed to fetch voices: {e}")
            return None

    def get_user_info(self) -> Optional[dict]:
        """Get user account information.
        
        Returns:
            User info dict or None if failed
        """
        url = f"{ELEVENLABS_API_URL}/user"
        
        try:
            logger.info("Fetching user information")
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                logger.error(f"API error: {response.status_code}")
                return None
            
            user_info = response.json()
            logger.info(f"User subscription: {user_info.get('subscription', {}).get('tier')}")
            return user_info
        except Exception as e:
            logger.error(f"Failed to fetch user info: {e}")
            return None
