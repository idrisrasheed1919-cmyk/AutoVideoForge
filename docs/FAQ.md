"""FAQ - Frequently Asked Questions."""

# FAQ

## General

### How long does it take to generate a video?

Typical times for 60-second video:
- Script generation: 10-30 seconds
- Voice synthesis: 20-60 seconds
- Scene rendering: 30-120 seconds
- Video composition: 30-60 seconds
- **Total**: 2-5 minutes

Times vary based on:
- Video quality setting
- Video duration
- Internet speed (for API calls)
- Computer specifications

### What video quality should I use?

- **Low**: Fast, great for testing (720p, 2 Mbps)
- **Medium**: Good balance (1080p, 5 Mbps)
- **High**: Professional (1080p, 8 Mbps) - Recommended
- **Ultra**: 4K quality (2160p, 15 Mbps) - Slow

### Can I customize the video style?

Currently limited customization. Future versions will include:
- Custom backgrounds and transitions
- Multiple scene layouts
- Background music
- Font selection
- Color schemes

## Technical

### Do I need all API keys?

Required:
- **ELEVENLABS_API_KEY**: For voice generation (required)

Choose one:
- **GEMINI_API_KEY**: For script generation (recommended, free tier)
- **OPENAI_API_KEY**: Alternative to Gemini

### Can I use local models instead of APIs?

Not yet. Current version requires APIs:
- Gemini or OpenAI for script generation
- ElevenLabs for voice synthesis

Future versions may support:
- Local LLMs (Llama, Mistral)
- Local TTS engines

### What audio formats are supported?

Input:
- WAV, MP3, M4A, OGG

Output:
- WAV (voice synthesis)
- AAC (in final video)

### What video formats are supported?

Output only:
- MP4 (H.264 + AAC)

Future: MKV, WebM, ProRes

## Troubleshooting

### Why is my video silent?

Common causes:
1. ElevenLabs API key invalid
2. Internet connection issue
3. Voice synthesis failed (check logs)

Fix:
1. Verify ElevenLabs key in .env
2. Check internet connection
3. Run with --debug flag
4. Check logs: `tail -f logs/app.log`

### Why is rendering so slow?

Causes:
1. High resolution/bitrate
2. Long video duration
3. Low system specs
4. FFmpeg version issues

Fix:
1. Use lower quality: `--quality "low"`
2. Shorter duration: `--duration 30`
3. Lower bitrate in .env
4. Close other applications

### Can I interrupt video generation?

Yes: Press Ctrl+C to stop. Temporary files will be cleaned up.

## Costs

### How much do the APIs cost?

**Gemini API**: Free tier available (60 requests/minute)
**ElevenLabs**: 
- Free tier: 10,000 characters/month
- Pro: $11+/month

### How many requests per month?

60-second video = ~1,500 characters
- Free tier: ~6-7 videos/month
- Pro tier: Unlimited

## Limitations

### What are current limitations?

1. No custom backgrounds/overlays
2. Basic scene generation
3. Limited voice options
4. No video editing capabilities
5. No subtitle generation

### What's coming next?

- Custom templates and themes
- Multiple scene types
- Auto-generated subtitles
- Music library integration
- Image/video library
- Batch processing
- Web UI

## More Help

- [Installation Guide](./INSTALLATION.md)
- [Quick Start](./QUICKSTART.md)
- [Configuration](./CONFIGURATION.md)
- [Troubleshooting](./TROUBLESHOOTING.md)
- [GitHub Issues](https://github.com/idrisrasheed1919-cmyk/AutoVideoForge/issues)
