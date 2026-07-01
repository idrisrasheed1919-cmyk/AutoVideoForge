"""TTS provider abstraction for multiple services."""

from typing import Optional
from pathlib import Path
from enum import Enum

from api.elevenlabs_client import ElevenLabsClient
from utils.logger import get_logger

logger = get_logger(__name__)


class TTSProvider(Enum):
    """TTS provider options."""
    ELEVENLABS = "elevenlabs"


class TTSManager:
    """Manage text-to-speech operations."""

    def __init__(self, api_key: str, provider: TTSProvider = TTSProvider.ELEVENLABS):
        """Initialize TTS manager.
        
        Args:
            api_key: API key for TTS provider
            provider: TTS provider to use
        """
        self.provider = provider
        
        if provider == TTSProvider.ELEVENLABS:
            self.client = ElevenLabsClient(api_key)
        else:
            raise ValueError(f"Unsupported TTS provider: {provider}")
        
        logger.info(f"TTS manager initialized with provider: {provider.value}")

    def synthesize(
        self,
        text: str,
        output_path: Path,
        **kwargs,
    ) -> bool:
        """Synthesize text to speech.
        
        Args:
            text: Text to synthesize
            output_path: Output audio file path
            **kwargs: Provider-specific options
            
        Returns:
            True if successful, False otherwise
        """
        if self.provider == TTSProvider.ELEVENLABS:
            stability = kwargs.get("stability", 0.5)
            return self.client.text_to_speech(text, output_path, stability=stability)
        
        return False
