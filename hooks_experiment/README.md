# hooks_experiment

## About This Project

This is a Python project designed for experimenting with Claude Code hooks functionality. The project includes:

- **Sound Playing Application**: A simple Python script (`play_sound.py`) that uses pygame to play audio files
- **Audio File**: Contains a sound file (`ulala.wav`) for testing audio playback
- **Python Environment**: Set up with uv for dependency management and virtual environment
- **Claude Code Integration**: Used as a testing ground for understanding Claude Code behavior, tool usage, and hooks configuration

## Claude Code Learning Notes

### Session Management
- Claude Code does not retain conversation history between sessions
- When you run `/exit` and reopen Claude, it starts fresh without memory of previous conversations
- Each new session is independent and doesn't have access to prior interaction history

### Tool Usage and Hooks
- Claude Code can be blocked from executing certain tool operations based on user preferences or hooks configuration
- When a tool use is rejected, Claude will stop and wait for user guidance on how to proceed
- Hooks are shell commands that execute in response to events like tool calls
- Hook feedback is treated as coming from the user
- Users can configure hooks in settings to control Claude's behavior during sessions

### File Operations
- Claude Code may have built-in protective measures for file modifications
- Blocking can occur even when no explicit hooks are configured
- The system can prevent file writes and prompt for user confirmation