"""Tests for audio processing."""

import pytest
from pathlib import Path
from audio.audio_processor import AudioProcessor
from pydub import AudioSegment


class TestAudioProcessor:
    """Test audio processing."""

    def test_initialization(self):
        """Test audio processor initialization."""
        processor = AudioProcessor(sample_rate=44100)
        assert processor.sample_rate == 44100

    def test_get_duration(self):
        """Test getting audio duration."""
        processor = AudioProcessor()
        audio = AudioSegment.silent(duration=5000)  # 5 seconds
        
        duration = processor.get_duration(audio)
        assert abs(duration - 5.0) < 0.1  # Allow 100ms tolerance

    def test_adjust_volume(self):
        """Test volume adjustment."""
        processor = AudioProcessor()
        audio = AudioSegment.silent(duration=1000)
        
        louder = processor.adjust_volume(audio, 6)  # +6dB
        assert len(louder) > 0

    def test_add_silence(self):
        """Test adding silence."""
        processor = AudioProcessor()
        audio = AudioSegment.silent(duration=1000)
        
        with_silence = processor.add_silence(audio, 1000, position="end")
        duration = processor.get_duration(with_silence)
        
        assert abs(duration - 2.0) < 0.1  # 2 seconds total
