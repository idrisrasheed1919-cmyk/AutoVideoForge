"""Quick start guide."""

# Quick Start Guide

## 1. Setup (First Time)

```bash
# Clone repository
git clone https://github.com/idrisrasheed1919-cmyk/AutoVideoForge.git
cd AutoVideoForge

# Run setup
python scripts/setup.py
# OR
# Windows: .scripts\setup_windows.bat
# Linux/macOS: ./.scripts/setup_linux.sh
```

## 2. Configure API Keys

```bash
# Copy template
cp .env.example .env

# Edit .env and add your API keys
# GEMINI_API_KEY=your_key_here
# ELEVENLABS_API_KEY=your_key_here
```

## 3. Generate Your First Video

```bash
# Basic usage
python main.py --topic "artificial intelligence"

# With custom duration and tone
python main.py --topic "machine learning" --duration 120 --tone "educational"

# With high quality output
python main.py --topic "Python programming" --quality "high"

# Debug mode
python main.py --topic "web development" --debug
```

## 4. Find Your Video

Generated files are in the `output/` directory:
- `video_YYYYMMDD_HHMMSS.mp4` - Final video
- `audio_YYYYMMDD_HHMMSS.wav` - Audio track
- `script_YYYYMMDD_HHMMSS.txt` - Generated script
- `thumbnail_YYYYMMDD_HHMMSS.png` - Thumbnail image

## Available Options

```bash
python main.py --help

Options:
  --topic TEXT           Video topic (required)
  --duration INTEGER     Target duration in seconds (default: 60)
  --tone TEXT            Script tone - informative, entertaining, educational,
                         formal, casual, professional (default: informative)
  --quality TEXT         Output quality - low, medium, high, ultra
                         (default: high)
  --debug                Enable debug logging
  --help                 Show help message
```

## Example Commands

```bash
# Generate 2-minute technology video
python main.py --topic "blockchain technology" --duration 120

# Generate entertaining video
python main.py --topic "funny cat facts" --tone "entertaining"

# Generate educational content with ultra quality
python main.py --topic "quantum computing" --tone "educational" --quality "ultra"

# Generate with debug output
python main.py --topic "AI trends 2024" --debug
```

## Troubleshooting

If you get FFmpeg errors:
1. Verify FFmpeg is installed: `ffmpeg -version`
2. Update FFMPEG_PATH in .env if needed
3. See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) for more help

If you get API key errors:
1. Verify .env file exists: `cp .env.example .env`
2. Verify API keys are correct in .env
3. Test API key in respective dashboard

See [FAQ.md](./FAQ.md) for more common questions.
