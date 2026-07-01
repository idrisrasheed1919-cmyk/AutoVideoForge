"""File management utilities."""

from pathlib import Path
from typing import Optional, List
import shutil
import os

from utils.logger import get_logger

logger = get_logger(__name__)


class FileManager:
    """Manage file operations."""

    @staticmethod
    def ensure_dir(directory: Path) -> Path:
        """Ensure directory exists.
        
        Args:
            directory: Directory path
            
        Returns:
            Directory path
        """
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Ensured directory exists: {directory}")
        return directory

    @staticmethod
    def safe_delete(path: Path, recursive: bool = False) -> bool:
        """Safely delete file or directory.
        
        Args:
            path: Path to delete
            recursive: Delete directory recursively
            
        Returns:
            True if successful, False otherwise
        """
        try:
            path = Path(path)
            if path.is_file():
                path.unlink()
                logger.debug(f"Deleted file: {path}")
                return True
            elif path.is_dir():
                if recursive:
                    shutil.rmtree(path)
                    logger.debug(f"Deleted directory recursively: {path}")
                else:
                    path.rmdir()
                    logger.debug(f"Deleted empty directory: {path}")
                return True
        except Exception as e:
            logger.error(f"Failed to delete {path}: {e}")
            return False
        return False

    @staticmethod
    def copy_file(source: Path, destination: Path, overwrite: bool = False) -> bool:
        """Copy file safely.
        
        Args:
            source: Source file path
            destination: Destination file path
            overwrite: Overwrite if destination exists
            
        Returns:
            True if successful, False otherwise
        """
        try:
            source = Path(source)
            destination = Path(destination)
            
            if destination.exists() and not overwrite:
                logger.warning(f"Destination exists and overwrite=False: {destination}")
                return False
            
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            logger.debug(f"Copied {source} to {destination}")
            return True
        except Exception as e:
            logger.error(f"Failed to copy file: {e}")
            return False

    @staticmethod
    def get_file_size(path: Path) -> Optional[int]:
        """Get file size in bytes.
        
        Args:
            path: File path
            
        Returns:
            File size or None if file doesn't exist
        """
        try:
            path = Path(path)
            return path.stat().st_size
        except Exception as e:
            logger.error(f"Failed to get file size: {e}")
            return None

    @staticmethod
    def cleanup_temp_files(directory: Path, extensions: Optional[List[str]] = None) -> int:
        """Clean up temporary files.
        
        Args:
            directory: Directory to clean
            extensions: File extensions to delete (e.g., ['.tmp', '.log'])
            
        Returns:
            Number of files deleted
        """
        if extensions is None:
            extensions = [".tmp", ".log", ".cache"]
        
        count = 0
        try:
            directory = Path(directory)
            if not directory.exists():
                return count
            
            for file in directory.rglob("*"):
                if file.is_file() and file.suffix in extensions:
                    if FileManager.safe_delete(file):
                        count += 1
        except Exception as e:
            logger.error(f"Failed to cleanup temp files: {e}")
        
        logger.info(f"Cleaned up {count} temporary files")
        return count
