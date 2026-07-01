"""Troubleshooting guide."""

# Troubleshooting Guide

## Common Issues

### FFmpeg Not Found

**Error**: `ffmpeg: command not found`

**Solutions**:
1. **Windows**: Download from https://ffmpeg.org/download.html and add to PATH
2. **Linux**: `sudo apt-get install ffmpeg`
3. **macOS**: `brew install ffmpeg`
4. Set FFMPEG_PATH in .env to full path if needed

### API Key Invalid

**Error**: `API key is invalid or has expired`

**Solutions**:
1. Verify .env file exists and is readable
2. Check API key format (no extra spaces)
3. Regenerate API key in provider dashboard
4. Ensure ELEVENLABS_API_KEY is set (required)

### Video Generation Timeout

**Error**: `Rendering timed out after 3600 seconds`

**Solutions**:
1. Reduce video quality: `--quality "low"`
2. Reduce duration: `--duration 30`
3. Lower resolution in .env:
   ```env
   VIDEO_WIDTH=1280
   VIDEO_HEIGHT=720
   ```
4. Increase timeout: `RENDER_TIMEOUT=7200` in .env

### Out of Memory

**Error**: `MemoryError` or system becomes unresponsive

**Solutions**:
1. Reduce resolution
2. Lower FPS: `VIDEO_FPS=24`
3. Generate shorter videos: `--duration 30`
4. Close other applications
5. Add more RAM or use lower quality settings

### Audio Out of Sync

**Error**: Video plays but audio doesn't match

**Solutions**:
1. Check audio file duration
2. Verify ElevenLabs API is working
3. Check AUDIO_SAMPLE_RATE: 44100 recommended
4. Look at logs: `tail -f logs/app.log`

### Python Version Mismatch

**Error**: `Python 3.10+ required`

**Solution**: Install Python 3.10+
- Windows: https://www.python.org/downloads/
- Linux: `sudo apt-get install python3.10`
- macOS: `brew install python@3.10`

### Dependencies Won't Install

**Error**: `pip install fails` or `ModuleNotFoundError`

**Solutions**:
1. Upgrade pip: `pip install --upgrade pip`
2. Create fresh virtual environment: `rm -rf venv && python -m venv venv`
3. Use specific Python version: `python3.10 -m pip install -r requirements.txt`
4. Check Python compatibility

## Getting Help

1. **Check logs**: `tail -f logs/app.log`
2. **Run with debug**: `python main.py --topic "test" --debug`
3. **See FAQ**: Read [FAQ.md](./FAQ.md)
4. **Report issues**: https://github.com/idrisrasheed1919-cmyk/AutoVideoForge/issues
