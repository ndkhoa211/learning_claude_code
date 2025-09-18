# hooks_experiment

## About This Project

This is a Python experimental project for learning and testing Claude Code hooks functionality. The main application is a pygame-based audio player that plays sound files, with integrated Claude Code hooks for event-driven audio feedback.

## Project Structure

```
hooks_experiment/
├── play_sound.py          # Main pygame-based audio player application
├── ulala.wav             # Test audio file (96KB WAV format)
├── pyproject.toml        # UV package configuration
├── .python-version       # Python 3.12+ requirement
├── CLAUDE.md             # Instructions for Claude Code instances
├── .venv/                # Virtual environment (UV managed)
└── .claude/              # Claude Code configuration
    └── settings.local.json
```

## Development Setup

This project uses UV as the Python package manager:

```bash
# Install/sync dependencies
uv sync

# Run the main application
uv run play_sound.py

# Add new dependencies
uv add <package>

# Remove dependencies
uv remove <package>
```

## Requirements

- **Python**: 3.12+ (specified in `.python-version`)
- **Audio System**: Working audio output and pygame compatibility
- **Package Manager**: UV (not pip)
- **Dependencies**: pygame >= 2.0.0

## Claude Code Integration

### Project Instructions
The project includes `CLAUDE.md` with instructions for Claude Code instances:
- **Purpose**: Provides context and guidance for Claude Code when working in this repository
- **Contains**: Project overview, development commands, architecture details, and requirements
- **Scope**: Instructions that override default Claude Code behavior for this project

### Hooks Configuration
The project has active hooks configured in `.claude/settings.local.json`:
- **Hook Type**: "Stop" event hook that triggers `uv run play_sound.py`
- **Purpose**: Provides audio feedback when Claude Code encounters stop events
- **Behavior**: Hook responses are treated as user input

### Learning Notes
- **Session Management**: Claude Code doesn't retain conversation history between sessions
- **Tool Usage**: Claude can be blocked from certain operations based on hooks configuration
- **File Operations**: Built-in protective measures may prevent file modifications
- **Event-Driven**: Hooks execute shell commands in response to specific events

## Usage

Run the audio player directly:
```bash
uv run play_sound.py
```

The application will play the `ulala.wav` file and provide console output about the playbook status.