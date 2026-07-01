#!/usr/bin/env python
"""Setup configuration for AI Video Automation System."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="auto-video-forge",
    version="1.0.0",
    author="Video Automation Team",
    author_email="support@example.com",
    description="AI-powered video generation system with script, voice, and rendering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/idrisrasheed1919-cmyk/AutoVideoForge",
    project_urls={
        "Bug Tracker": "https://github.com/idrisrasheed1919-cmyk/AutoVideoForge/issues",
        "Documentation": "https://github.com/idrisrasheed1919-cmyk/AutoVideoForge#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "moviepy==1.0.3",
        "Pillow==10.1.0",
        "numpy==1.26.2",
        "scipy==1.11.4",
        "pydub==0.25.1",
        "requests==2.31.0",
        "google-generativeai==0.3.0",
        "openai==1.3.8",
        "elevenlabs==0.2.27",
        "python-dotenv==1.0.0",
        "pydantic==2.5.0",
        "pydantic-settings==2.1.0",
        "coloredlogs==15.0.1",
        "rich==13.7.0",
        "click==8.1.7",
        "typer==0.9.0",
        "validators==0.22.0",
    ],
    extras_require={
        "dev": [
            "pytest==7.4.3",
            "pytest-cov==4.1.0",
            "pytest-mock==3.12.0",
            "black==23.12.0",
            "flake8==6.1.0",
            "mypy==1.7.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "auto-video=cli.main:app",
        ],
    },
)
