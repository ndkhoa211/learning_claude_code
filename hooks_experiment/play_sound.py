import pygame
import os
import sys
from pathlib import Path

def main():
    # Get the directory where the script is located
    script_dir = Path(__file__).parent
    sound_file = script_dir / "ulala.wav"

    # Check if the sound file exists
    if not sound_file.exists():
        print(f"Error: Sound file not found at {sound_file}")
        sys.exit(1)

    # Initialize pygame mixer
    pygame.mixer.init()

    try:
        # Load and play the sound
        sound = pygame.mixer.Sound(str(sound_file))
        sound.play()

        # Wait for the sound to finish playing
        while pygame.mixer.get_busy():
            pygame.time.wait(100)

        print("Sound played successfully!")

    except pygame.error as e:
        print(f"Error playing sound: {e}")
        sys.exit(1)

    finally:
        pygame.mixer.quit()

if __name__ == "__main__":
    main()
