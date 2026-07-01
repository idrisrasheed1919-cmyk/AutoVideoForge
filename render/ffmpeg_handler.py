"""FFmpeg wrapper and handler."""

from typing import Optional, List
from pathlib import Path
import subprocess
import json

from utils.logger import get_logger
from config.settings import settings

logger = get_logger(__name__)


class FFmpegHandler:
    """Handle FFmpeg operations."""

    def __init__(self, ffmpeg_path: str = "ffmpeg", ffprobe_path: str = "ffprobe"):
        """Initialize FFmpeg handler.
        
        Args:
            ffmpeg_path: Path to ffmpeg executable
            ffprobe_path: Path to ffprobe executable
        """
        self.ffmpeg_path = ffmpeg_path
        self.ffprobe_path = ffprobe_path
        
        # Check if ffmpeg is available
        if not self._check_ffmpeg():
            logger.warning("FFmpeg not found in PATH")
        else:
            logger.info("FFmpeg initialized successfully")

    def _check_ffmpeg(self) -> bool:
        """Check if FFmpeg is available.
        
        Returns:
            True if FFmpeg is available
        """
        try:
            subprocess.run(
                [self.ffmpeg_path, "-version"],
                capture_output=True,
                timeout=5,
                check=True,
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def get_video_info(self, video_path: Path) -> Optional[dict]:
        """Get video information using ffprobe.
        
        Args:
            video_path: Path to video file
            
        Returns:
            Dictionary with video info or None if failed
        """
        try:
            cmd = [
                self.ffprobe_path,
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                "-show_streams",
                str(video_path),
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, check=True)
            info = json.loads(result.stdout)
            logger.debug(f"Video info retrieved for {video_path}")
            return info
        except Exception as e:
            logger.error(f"Failed to get video info: {e}")
            return None

    def get_duration(self, media_path: Path) -> Optional[float]:
        """Get media duration in seconds.
        
        Args:
            media_path: Path to media file
            
        Returns:
            Duration in seconds or None if failed
        """
        info = self.get_video_info(media_path)
        if info and "format" in info:
            duration = float(info["format"].get("duration", 0))
            logger.debug(f"Duration: {duration}s")
            return duration
        return None

    def concat_videos(
        self,
        video_list: List[Path],
        output_path: Path,
        **kwargs,
    ) -> bool:
        """Concatenate multiple videos.
        
        Args:
            video_list: List of video file paths
            output_path: Output video path
            **kwargs: Additional ffmpeg options
            
        Returns:
            True if successful
        """
        if not video_list:
            logger.error("Video list is empty")
            return False
        
        try:
            # Create concat demuxer file
            concat_file = output_path.parent / "concat.txt"
            with open(concat_file, "w") as f:
                for video in video_list:
                    f.write(f"file '{video.absolute()}'\n")
            
            cmd = [
                self.ffmpeg_path,
                "-f", "concat",
                "-safe", "0",
                "-i", str(concat_file),
                "-c", "copy",
                "-y",
                str(output_path),
            ]
            
            logger.info(f"Concatenating {len(video_list)} videos...")
            subprocess.run(cmd, timeout=settings.render_timeout, check=True)
            
            # Cleanup concat file
            concat_file.unlink()
            logger.info(f"Videos concatenated: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to concatenate videos: {e}")
            return False

    def merge_audio_video(
        self,
        video_path: Path,
        audio_path: Path,
        output_path: Path,
        **kwargs,
    ) -> bool:
        """Merge audio with video.
        
        Args:
            video_path: Path to video file
            audio_path: Path to audio file
            output_path: Output file path
            **kwargs: Additional ffmpeg options
            
        Returns:
            True if successful
        """
        try:
            cmd = [
                self.ffmpeg_path,
                "-i", str(video_path),
                "-i", str(audio_path),
                "-c:v", settings.video_codec,
                "-c:a", "aac",
                "-map", "0:v:0",
                "-map", "1:a:0",
                "-shortest",
                "-y",
                str(output_path),
            ]
            
            logger.info("Merging audio and video...")
            subprocess.run(cmd, timeout=settings.render_timeout, check=True)
            logger.info(f"Audio/video merged: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to merge audio/video: {e}")
            return False

    def extract_frame(
        self,
        video_path: Path,
        output_path: Path,
        timestamp: float = 0.0,
    ) -> bool:
        """Extract frame from video.
        
        Args:
            video_path: Path to video file
            output_path: Output image path
            timestamp: Timestamp in seconds to extract
            
        Returns:
            True if successful
        """
        try:
            cmd = [
                self.ffmpeg_path,
                "-ss", str(timestamp),
                "-i", str(video_path),
                "-vframes", "1",
                "-y",
                str(output_path),
            ]
            
            logger.info(f"Extracting frame at {timestamp}s...")
            subprocess.run(cmd, timeout=30, check=True, capture_output=True)
            logger.info(f"Frame extracted: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to extract frame: {e}")
            return False
