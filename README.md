# AutoVideoForge - AI Video Automation System

A production-ready system for automatically generating full-length videos with AI scripts, voice synthesis, and professional rendering.

## 🎯 Features

- ✅ **End-to-End Video Generation**: Script → Voice → Visuals → MP4
- ✅ **AI Script Generation**: Powered by Gemini/OpenAI APIs
- ✅ **Realistic Voice Synthesis**: ElevenLabs TTS integration
- ✅ **Auto-synced Audio**: No silent clips or cutoffs
- ✅ **Professional Rendering**: FFmpeg-based high-quality video generation
- ✅ **Thumbnail Generation**: Automatic poster images
- ✅ **Logging & Error Handling**: Comprehensive debugging and logs
- ✅ **Windows/Linux/Mac Compatible**: Cross-platform support
- ✅ **One-Command Execution**: `python main.py` to generate video

## 📋 Prerequisites

### System Requirements
- Python 3.10+
- FFmpeg (auto-detected or guided installation)
- 4GB RAM minimum
- 10GB free disk space

### Windows Users
- Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
- Or run: `.\.scripts\setup_windows.bat`

### Linux/Mac Users
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/idrisrasheed1919-cmyk/AutoVideoForge.git
cd AutoVideoForge
```

### 2. Setup Environment

**Option A: Automatic Setup (Recommended)**
```bash
python scripts/setup.py
```

**Option B: Manual Setup**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Keys

Copy `.env.example` to `.env` and add your API keys:
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```
GEMINI_API_KEY=your_key_here
ELEVENLABS_API_KEY=your_key_here
```

### 4. Generate Video

```bash
# Default: Generates a video about technology
python main.py

# Custom topic
python main.py --topic "artificial intelligence"

# Specific length (in seconds)
python main.py --topic "Python programming" --duration 120

# With debug logging
python main.py --debug
```

### 5. Output

Generated files will be in `./output/`:
```
output/
├── video_<timestamp>.mp4      # Final video
├── audio_<timestamp>.wav      # Generated audio track
├── script_<timestamp>.txt     # Generated script
└── thumbnail_<timestamp>.png  # Video thumbnail
```

## 📁 Project Structure

```
AutoVideoForge/
├── core/                      # Video engine and pipeline
│   ├── __init__.py
│   ├── video_engine.py        # Main video pipeline
│   ├── scene_builder.py       # Scene composition
│   └── timeline.py            # Timeline management
├── audio/                     # Audio processing
│   ├── __init__.py
│   ├── tts_provider.py        # TTS API handlers
│   ├── audio_processor.py     # Audio editing
│   └── voice_sync.py          # Voice-video sync
├── scripts/                   # Script generation
│   ├── __init__.py
│   ├── script_generator.py    # AI script creation
│   ├── content_parser.py      # Script parsing
│   └── setup.py               # Auto-setup script
├── assets/                    # Media templates
│   ├── images/                # Background images
│   ├── music/                 # Background music
│   ├── fonts/                 # Custom fonts
│   └── templates/             # Scene templates
├── render/                    # Rendering engine
│   ├── __init__.py
│   ├── ffmpeg_handler.py      # FFmpeg wrapper
│   ├── video_composer.py      # Video assembly
│   └── quality_controller.py  # Quality management
├── api/                       # External API handlers
│   ├── __init__.py
│   ├── gemini_client.py       # Gemini API client
│   ├── openai_client.py       # OpenAI API client
│   └── elevenlabs_client.py   # ElevenLabs API client
├── utils/                     # Utilities
│   ├── __init__.py
│   ├── logger.py              # Logging setup
│   ├── config.py              # Config loader
│   ├── file_manager.py        # File operations
│   ├── validators.py          # Input validation
│   └── time_utils.py          # Time/duration helpers
├── config/                    # Configuration
│   ├── __init__.py
│   ├── settings.py            # Global settings
│   ├── defaults.py            # Default values
│   └── env_loader.py          # Environment loader
├── cli/                       # Command-line interface
│   ├── __init__.py
│   ├── main.py                # CLI entry point
│   ├── commands.py            # Command handlers
│   └── validators.py          # CLI validators
├── tests/                     # Unit tests
│   ├── __init__.py
│   ├── test_script_generator.py
│   ├── test_video_engine.py
│   ├── test_audio_processor.py
│   └── test_integration.py
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── README.md                  # This file
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
└── LICENSE                    # MIT License
```

## ⚙️ Configuration

### Video Quality Settings

Edit `.env` to adjust:

```env
# Resolution
VIDEO_WIDTH=1920
VIDEO_HEIGHT=1080

# Frame rate
VIDEO_FPS=30

# Bitrate (higher = better quality, larger file)
VIDEO_BITRATE=8000k
AUDIO_BITRATE=192k
```

### API Configuration

**Gemini API** (Recommended - free tier available):
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikeys)
2. Click "Create API Key"
3. Add to `.env`: `GEMINI_API_KEY=your_key`

**ElevenLabs API** (For voice synthesis):
1. Sign up at [elevenlabs.io](https://elevenlabs.io)
2. Get API key from settings
3. Add to `.env`: `ELEVENLABS_API_KEY=your_key`

## 🎬 Workflow

### Video Generation Pipeline

```
1. Script Generation
   └─> AI generates coherent script (60-300 seconds)

2. Script Parsing
   └─> Extract duration and segment markers

3. Voice Synthesis
   └─> Convert script to audio with ElevenLabs

4. Scene Building
   └─> Create visual scenes matching audio duration

5. Video Composition
   └─> Combine scenes with audio track

6. Rendering
   └─> FFmpeg encodes to final MP4

7. Thumbnail Generation
   └─> Extract key frame for poster
```

## 🐛 Troubleshooting

### "FFmpeg not found"
```bash
# Windows: Download from ffmpeg.org
# Linux: sudo apt-get install ffmpeg
# Mac: brew install ffmpeg
```

### "API Key Invalid"
- Verify `.env` file exists and is readable
- Check API key format (no extra spaces)
- Test API key in respective dashboard

### "Audio out of sync"
- Check audio duration matches script duration
- Verify sample rate: 44100 Hz recommended
- Review logs: `tail -f logs/app.log`

### "Video generation timeout"
- Reduce video resolution in `.env`
- Lower bitrate settings
- Increase `RENDER_TIMEOUT` value

### "Out of memory"
- Reduce resolution
- Lower FPS from 30 to 24
- Process videos sequentially (not parallel)

## 📊 Logging

All operations are logged to `logs/app.log`:

```bash
# View logs
tail -f logs/app.log

# Enable debug logging
export LOG_LEVEL=DEBUG
python main.py
```

## 📦 Dependencies

- **moviepy**: Video composition
- **pydub**: Audio processing
- **requests**: HTTP client
- **python-dotenv**: Environment management
- **pydantic**: Data validation
- **google-generativeai**: Gemini API
- **openai**: OpenAI API
- **elevenlabs**: ElevenLabs API

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_script_generator.py -v

# With coverage
python -m pytest tests/ --cov=. --cov-report=html
```

## 🤝 Contributing

1. Fork repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📝 License

MIT License - see LICENSE file for details

## 💬 Support

- 📖 [Documentation](./docs/)
- 🐛 [Report Issues](https://github.com/idrisrasheed1919-cmyk/AutoVideoForge/issues)
- 💬 [Discussions](https://github.com/idrisrasheed1919-cmyk/AutoVideoForge/discussions)

## 📚 Additional Resources

- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [MoviePy Guide](https://zulko.github.io/moviepy/)
- [Gemini API Docs](https://ai.google.dev/docs)
- [ElevenLabs Docs](https://elevenlabs.io/docs)

---

**Made with ❤️ for content creators and automation enthusiasts**
