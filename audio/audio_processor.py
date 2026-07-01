"""Audio processing and manipulation."""

from typing import Optional, Tuple
from pathlib import Path
import numpy as np
from pydub import AudioSegment
from pydub.effects import normalize

from utils.logger import get_logger

logger = get_logger(__name__)


class AudioProcessor:
    """Process and manipulate audio files."""

    def __init__(self, sample_rate: int = 44100):
        """Initialize audio processor.
        
        Args:
            sample_rate: Sample rate for audio (Hz)
        """
        self.sample_rate = sample_rate

    def load_audio(self, file_path: Path) -> Optional[AudioSegment]:
        """Load audio file.
        
        Args:
            file_path: Path to audio file
            
        Returns:
            AudioSegment or None if failed
        """
        try:
            logger.info(f"Loading audio from {file_path}")
            audio = AudioSegment.from_file(str(file_path))
            logger.info(f"Audio loaded: {len(audio)}ms duration")
            return audio
        except Exception as e:
            logger.error(f"Failed to load audio: {e}")
            return None

    def save_audio(
        self,
        audio: AudioSegment,
        output_path: Path,
        format: str = "wav",
    ) -> bool:
        """Save audio file.
        
        Args:
            audio: AudioSegment to save
            output_path: Output file path
            format: Audio format (wav, mp3, m4a, etc.)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            audio.export(str(output_path), format=format)
            logger.info(f"Audio saved to {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to save audio: {e}")
            return False

    def get_duration(self, audio: AudioSegment) -> float:
        """Get audio duration in seconds.
        
        Args:
            audio: AudioSegment
            
        Returns:
            Duration in seconds
        """
        return len(audio) / 1000.0

    def concatenate_audio(self, audio_list: list) -> Optional[AudioSegment]:
        """Concatenate multiple audio segments.
        
        Args:
            audio_list: List of AudioSegment objects
            
        Returns:
            Concatenated AudioSegment or None if failed
        """
        try:
            if not audio_list:
                logger.error("Audio list is empty")
                return None
            
            combined = audio_list[0]
            for audio in audio_list[1:]:
                combined += audio
            
            logger.info(f"Concatenated {len(audio_list)} audio segments")
            return combined
        except Exception as e:
            logger.error(f"Failed to concatenate audio: {e}")
            return None

    def adjust_volume(self, audio: AudioSegment, gain_db: float) -> AudioSegment:
        """Adjust volume of audio.
        
        Args:
            audio: AudioSegment to adjust
            gain_db: Gain in decibels (positive = louder, negative = quieter)
            
        Returns:
            Volume-adjusted AudioSegment
        """
        try:
            adjusted = audio + gain_db
            logger.info(f"Audio volume adjusted by {gain_db}dB")
            return adjusted
        except Exception as e:
            logger.error(f"Failed to adjust volume: {e}")
            return audio

    def normalize_audio(self, audio: AudioSegment) -> AudioSegment:
        """Normalize audio to target loudness.
        
        Args:
            audio: AudioSegment to normalize
            
        Returns:
            Normalized AudioSegment
        """
        try:
            normalized = normalize(audio)
            logger.info("Audio normalized")
            return normalized
        except Exception as e:
            logger.error(f"Failed to normalize audio: {e}")
            return audio

    def add_silence(
        self,
        audio: AudioSegment,
        duration_ms: int,
        position: str = "end",
    ) -> AudioSegment:
        """Add silence to audio.
        
        Args:
            audio: AudioSegment
            duration_ms: Duration of silence in milliseconds
            position: Position to add silence (start, end, both)
            
        Returns:
            AudioSegment with added silence
        """
        silence = AudioSegment.silent(duration=duration_ms)
        
        if position == "start":
            return silence + audio
        elif position == "end":
            return audio + silence
        elif position == "both":
            return silence + audio + silence
        else:
            logger.warning(f"Unknown position: {position}")
            return audio
