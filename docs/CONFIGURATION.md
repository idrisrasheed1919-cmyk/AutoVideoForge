"""Configuration guide."""

# Configuration Guide

## Environment Variables

Configuration is done through the `.env` file. Copy `.env.example` to `.env` and update values.

### API Keys

```env
# Gemini API (for script generation)
GEMINI_API_KEY=your_gemini_api_key_here

# OpenAI API (alternative)
OPENAI_API_KEY=your_openai_api_key_here

# ElevenLabs (for voice synthesis)
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM
```

### Video Settings

```env
# Resolution
VIDEO_WIDTH=1920
VIDEO_HEIGHT=1080

# Frame rate
VIDEO_FPS=30

# Bitrate (higher = better quality, larger file)
VIDEO_BITRATE=8000k
AUDIO_BITRATE=192k
AUDIO_SAMPLE_RATE=44100
```

### System Settings

```env
# Output directories
OUTPUT_DIR=./output
TEMP_DIR=./temp
CACHE_DIR=./cache

# Logging
LOG_LEVEL=INFO
DEBUG=false

# FFmpeg paths (auto-detected if not set)
FFMPEG_PATH=ffmpeg
FFPROBE_PATH=ffprobe
```

### Quality Presets

#### Low Quality (Fast rendering, smaller file)
```env
VIDEO_WIDTH=1280
VIDEO_HEIGHT=720
VIDEO_BITRATE=2000k
VIDEO_FPS=24
```

#### Medium Quality (Balanced)
```env
VIDEO_WIDTH=1920
VIDEO_HEIGHT=1080
VIDEO_BITRATE=5000k
VIDEO_FPS=30
```

#### High Quality (Recommended)
```env
VIDEO_WIDTH=1920
VIDEO_HEIGHT=1080
VIDEO_BITRATE=8000k
VIDEO_FPS=30
```

#### Ultra Quality (Slow rendering, large file)
```env
VIDEO_WIDTH=3840
VIDEO_HEIGHT=2160
VIDEO_BITRATE=15000k
VIDEO_FPS=30
```

## Getting API Keys

### Gemini API
1. Go to https://aistudio.google.com/app/apikeys
2. Click "Create API Key"
3. Copy the key to GEMINI_API_KEY in .env

### OpenAI API
1. Go to https://platform.openai.com/api-keys
2. Create a new secret key
3. Copy to OPENAI_API_KEY in .env

### ElevenLabs API
1. Sign up at https://elevenlabs.io
2. Go to settings → API Keys
3. Copy key to ELEVENLABS_API_KEY in .env
4. Find Voice ID from voices list for ELEVENLABS_VOICE_ID
