# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python experimental project for learning and testing Claude Code hooks functionality. The main application is a pygame-based audio player that plays sound files, with integrated Claude Code hooks for event-driven audio feedback.

## Development Commands

The project uses UV as the Python package manager:

- `uv run play_sound.py` - Execute the main sound playing application
- `uv sync` - Install/sync project dependencies
- `uv add <package>` - Add new dependencies
- `uv remove <package>` - Remove dependencies

## Architecture

- **Main Application**: `play_sound.py` - Pygame-based audio player for WAV files
- **Audio Asset**: `ulala.wav` - Test audio file (96KB)
- **Package Management**: UV with virtual environment in `.venv/`
- **Python Version**: 3.12+ required
- **Dependencies**: pygame >= 2.0.0

## Claude Code Hooks Configuration

The project has active hooks configured in `.claude/settings.local.json`:
- **Hook Type**: "Stop" event hook that triggers `uv run play_sound.py`
- **Purpose**: Provides audio feedback when Claude Code encounters stop events
- **Behavior**: Hook responses are treated as user input

## Key Requirements

1. **Audio System**: Requires working audio output and pygame compatibility
2. **UV Package Manager**: All dependency management uses UV, not pip
3. **Python 3.12+**: Specified in `.python-version`

## Important Notes

- This is an experimental learning project for Claude Code behavior
- No formal testing framework - testing is done manually via script execution
- Current git branch structure: working on `4_claude_code_commands`, main branch is `main`
- The project serves as both a functional audio application and a Claude Code learning laboratory
- I like to eat Vietnamese Pho