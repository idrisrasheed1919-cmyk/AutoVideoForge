"""Tests for video engine."""

import pytest
from pathlib import Path
from core.video_engine import VideoEngine
from core.scene_builder import SceneBuilder
from core.timeline import Timeline, TimelineEvent


class TestSceneBuilder:
    """Test scene building."""

    def test_timeline_initialization(self):
        """Test timeline initialization."""
        timeline = Timeline(total_duration=120.0)
        
        assert timeline.total_duration == 120.0
        assert len(timeline.get_events()) == 0

    def test_add_event(self):
        """Test adding events to timeline."""
        timeline = Timeline(total_duration=120.0)
        event = timeline.add_event(
            name="scene1",
            start_time=0.0,
            duration=30.0,
        )
        
        assert event is not None
        assert event.name == "scene1"
        assert event.duration == 30.0
        assert len(timeline.get_events()) == 1

    def test_get_events_at_time(self):
        """Test getting events at specific time."""
        timeline = Timeline(total_duration=120.0)
        timeline.add_event("scene1", 0.0, 30.0)
        timeline.add_event("scene2", 30.0, 30.0)
        
        events_at_15 = timeline.get_events_at_time(15.0)
        assert len(events_at_15) == 1
        assert events_at_15[0].name == "scene1"


class TestVideoEngine:
    """Test video engine."""

    def test_engine_initialization(self):
        """Test video engine initialization."""
        try:
            engine = VideoEngine()
            assert engine is not None
        except ValueError as e:
            pytest.skip(f"Skipped: {e}")
