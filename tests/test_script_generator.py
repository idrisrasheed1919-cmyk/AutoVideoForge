"""Tests for script generator."""

import pytest
from scripts.script_generator import ScriptGenerator
from scripts.content_parser import ScriptParser


class TestScriptGenerator:
    """Test script generation."""

    def test_script_generation(self):
        """Test basic script generation."""
        try:
            generator = ScriptGenerator()
            script = generator.generate(topic="Python programming", duration=30)
            
            assert script is not None
            assert len(script) > 0
            assert "Python" in script or "python" in script.lower()
        except ValueError as e:
            # API key not configured
            pytest.skip(f"Skipped: {e}")

    def test_invalid_topic(self):
        """Test invalid topic handling."""
        try:
            generator = ScriptGenerator()
            script = generator.generate(topic="", duration=30)
            assert script is None
        except ValueError:
            pytest.skip("API key not configured")


class TestScriptParser:
    """Test script parsing."""

    def test_parse_script(self):
        """Test script parsing."""
        script = "This is a test script. It has multiple sentences. And more content."
        duration, segments = ScriptParser.parse_script(script)
        
        assert duration > 0
        assert len(segments) > 0

    def test_extract_segments(self):
        """Test segment extraction."""
        script = "Part 1[SEGMENT]Part 2[SEGMENT]Part 3"
        segments = ScriptParser.extract_segments(script)
        
        assert len(segments) == 3
        assert "Part 1" in segments
        assert "Part 2" in segments
        assert "Part 3" in segments

    def test_remove_markers(self):
        """Test marker removal."""
        script = "Start[PAUSE]middle[EMPHASIS]end"
        cleaned = ScriptParser.remove_markers(script)
        
        assert "[PAUSE]" not in cleaned
        assert "[EMPHASIS]" not in cleaned
        assert "Start" in cleaned
        assert "middle" in cleaned
        assert "end" in cleaned
