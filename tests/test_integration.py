"""Integration tests."""

import pytest
from pathlib import Path
from config.settings import settings
from utils.file_manager import FileManager
from utils.validators import Validator


class TestIntegration:
    """Integration tests."""

    def test_settings_load(self):
        """Test settings loading."""
        assert settings is not None
        assert settings.output_dir.exists()
        assert settings.temp_dir.exists()

    def test_validators(self):
        """Test validators."""
        is_valid, error = Validator.validate_topic("artificial intelligence")
        assert is_valid
        assert error is None
        
        is_valid, error = Validator.validate_topic("")
        assert not is_valid
        assert error is not None

    def test_file_manager(self):
        """Test file manager."""
        test_dir = settings.temp_dir / "test"
        FileManager.ensure_dir(test_dir)
        assert test_dir.exists()
        
        FileManager.safe_delete(test_dir, recursive=True)
        assert not test_dir.exists()
