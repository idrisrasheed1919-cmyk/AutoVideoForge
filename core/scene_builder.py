"""Scene building and composition."""

from typing import Optional
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import imageio

from utils.logger import get_logger
from config.settings import settings
from utils.time_utils import TimeUtils

logger = get_logger(__name__)


class SceneBuilder:
    """Build video scenes and visual content."""

    def __init__(self):
        """Initialize scene builder."""
        self.width = settings.video_width
        self.height = settings.video_height
        self.fps = settings.video_fps
        logger.info(f"Scene builder initialized: {self.width}x{self.height} @ {self.fps}fps")

    def build_scenes(
        self,
        output_path: Path,
        duration: float,
        background_color: tuple = (20, 20, 40),
    ) -> bool:
        """Build video scenes using imageio.
        
        Args:
            output_path: Output video path
            duration: Total video duration
            background_color: RGB color tuple for background
            
        Returns:
            True if successful
        """
        try:
            logger.info(f"Building scenes for {duration}s video...")
            
            # Calculate number of frames
            num_frames = int(duration * self.fps)
            
            # Create frames
            frames = []
            for i in range(num_frames):
                # Create background frame
                frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
                frame[:] = background_color
                frames.append(frame)
            
            # Write video using imageio
            logger.info(f"Writing {len(frames)} frames to video...")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            writer = imageio.get_writer(str(output_path), fps=self.fps, codec='libx264')
            for frame in frames:
                writer.append_data(frame)
            writer.close()
            
            logger.info(f"Scenes built: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to build scenes: {e}")
            return False

    def create_text_frame(
        self,
        text: str,
        output_path: Path,
        font_size: int = 60,
        background_color: tuple = (20, 20, 40),
        text_color: tuple = (255, 255, 255),
    ) -> bool:
        """Create image with text.
        
        Args:
            text: Text to display
            output_path: Output image path
            font_size: Font size
            background_color: Background RGB color
            text_color: Text RGB color
            
        Returns:
            True if successful
        """
        try:
            # Create image
            img = Image.new(
                "RGB",
                (self.width, self.height),
                background_color,
            )
            
            draw = ImageDraw.Draw(img)
            
            # Calculate text position
            bbox = draw.textbbox((0, 0), text)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            x = (self.width - text_width) // 2
            y = (self.height - text_height) // 2
            
            # Draw text
            draw.text((x, y), text, fill=text_color)
            
            # Save image
            output_path.parent.mkdir(parents=True, exist_ok=True)
            img.save(output_path)
            logger.debug(f"Text frame created: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to create text frame: {e}")
            return False
