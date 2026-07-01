"""Main video engine and pipeline orchestrator."""

from typing import Optional, Dict
from pathlib import Path
from datetime import datetime

from scripts.script_generator import ScriptGenerator
from scripts.content_parser import ScriptParser
from audio.tts_provider import TTSManager
from audio.audio_processor import AudioProcessor
from core.scene_builder import SceneBuilder
from render.video_composer import VideoComposer
from render.quality_controller import QualityController
from config.settings import settings
from utils.logger import get_logger
from utils.file_manager import FileManager
from utils.time_utils import TimeUtils

logger = get_logger(__name__)


class VideoEngine:
    """Main video generation engine."""

    def __init__(self):
        """Initialize video engine."""
        self.script_generator = ScriptGenerator()
        self.tts_manager = TTSManager(settings.elevenlabs_api_key)
        self.audio_processor = AudioProcessor(settings.audio_sample_rate)
        self.scene_builder = SceneBuilder()
        self.video_composer = VideoComposer()
        self.quality_controller = QualityController()
        logger.info("Video engine initialized")

    def generate_video(
        self,
        topic: str,
        duration: int = 60,
        tone: str = "informative",
        quality: str = "high",
    ) -> Optional[Path]:
        """Generate complete video.
        
        Args:
            topic: Video topic
            duration: Target duration in seconds
            tone: Script tone
            quality: Output quality (low, medium, high, ultra)
            
        Returns:
            Path to generated video or None if failed
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        try:
            # Step 1: Generate script
            logger.info(f"\n=== STEP 1: GENERATING SCRIPT ===")
            script = self.script_generator.generate(
                topic=topic,
                duration=duration,
                tone=tone,
                save_to_file=True,
            )
            
            if not script:
                logger.error("Script generation failed")
                return None
            
            # Step 2: Parse script and estimate duration
            logger.info(f"\n=== STEP 2: PARSING SCRIPT ===")
            estimated_duration, segments = ScriptParser.parse_script(script)
            logger.info(f"Estimated duration: {estimated_duration:.1f}s ({len(segments)} segments)")
            
            # Step 3: Generate voice
            logger.info(f"\n=== STEP 3: GENERATING VOICE ===")
            audio_path = settings.output_dir / f"audio_{timestamp}.wav"
            
            if not self.tts_manager.synthesize(script, audio_path):
                logger.error("Voice synthesis failed")
                return None
            
            # Verify audio
            audio = self.audio_processor.load_audio(audio_path)
            if not audio:
                logger.error("Failed to load generated audio")
                return None
            
            actual_duration = self.audio_processor.get_duration(audio)
            logger.info(f"Audio generated: {actual_duration:.1f}s")
            
            # Step 4: Generate visuals
            logger.info(f"\n=== STEP 4: GENERATING VISUALS ===")
            video_path = settings.output_dir / f"video_temp_{timestamp}.mp4"
            
            if not self.scene_builder.build_scenes(video_path, actual_duration):
                logger.error("Scene building failed")
                return None
            
            # Step 5: Compose final video
            logger.info(f"\n=== STEP 5: COMPOSING VIDEO ===")
            final_video_path = settings.output_dir / f"video_{timestamp}.mp4"
            
            if not self.video_composer.add_audio_to_video(video_path, audio_path, final_video_path):
                logger.error("Video composition failed")
                return None
            
            # Step 6: Validate output
            logger.info(f"\n=== STEP 6: VALIDATING OUTPUT ===")
            is_valid, error = self.quality_controller.validate_output(final_video_path)
            
            if not is_valid:
                logger.error(f"Video validation failed: {error}")
                return None
            
            # Step 7: Generate thumbnail
            logger.info(f"\n=== STEP 7: GENERATING THUMBNAIL ===")
            thumbnail_path = settings.output_dir / f"thumbnail_{timestamp}.png"
            self.video_composer.generate_thumbnail(final_video_path, thumbnail_path)
            
            # Cleanup
            logger.info(f"\n=== CLEANUP ===")
            FileManager.safe_delete(video_path)
            
            logger.info(f"\n✅ VIDEO GENERATION COMPLETE")
            logger.info(f"Video: {final_video_path}")
            logger.info(f"Audio: {audio_path}")
            logger.info(f"Thumbnail: {thumbnail_path}")
            
            return final_video_path
        
        except Exception as e:
            logger.error(f"Video generation failed: {e}", exc_info=True)
            return None
