"""
Lyrics with Python - Animated Terminal Lyrics Display
====================================================

A dynamic lyrics visualization tool that creates animated, color-coded lyrics
display in the terminal with glitch effects and synchronized timing.

Author: 0PKunal  
License: MIT
"""

import random
import time
from typing import List, Tuple, Optional
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Initialize console with error handling
try:
    console = Console()
except Exception as e:
    print(f"Error initializing Rich console: {e}")
    exit(1)

# Configuration constants
GLITCH_SYMBOLS = ['#', '$', '%', '&', '/', '!', '?', '@', '*', '+', '~', '^']
DEFAULT_TYPING_SPEED = 0.07
DEFAULT_GLITCH_SPEED = 0.012
MIN_GLITCH_CYCLES = 2
MAX_GLITCH_CYCLES = 5

class LyricsAnimator:
    """Main class for handling lyrics animation and display."""

    def __init__(self, console: Console):
        """Initialize the animator with a Rich console instance."""
        self.console = console
        self.symbols = GLITCH_SYMBOLS

    def type_effect(self, text: str, color: str = "bold bright_white", 
                   speed: float = DEFAULT_TYPING_SPEED, 
                   glitch_speed: float = DEFAULT_GLITCH_SPEED) -> None:
        """
        Create typing effect with glitch animation for each character.

        Args:
            text: The text to display with animation
            color: Rich color string for the final text
            speed: Speed of typing animation (seconds per character)
            glitch_speed: Speed of glitch effect (seconds per cycle)
        """
        if not text.strip():
            return

        display = [" "] * len(text)

        for i in range(len(text)):
            # Glitch effect for current character
            glitch_cycles = random.randint(MIN_GLITCH_CYCLES, MAX_GLITCH_CYCLES)

            for _ in range(glitch_cycles):
                display[i] = random.choice(self.symbols)
                self.console.print("".join(display), end="\r", style="bold magenta")
                time.sleep(glitch_speed)

            # Reveal actual character
            display[i] = text[i]
            self.console.print("".join(display), end="\r", style=color)
            time.sleep(speed)

        # Final display with proper formatting
        self.console.print("".join(display), style=color)

    def choose_color(self, text: str) -> str:
        """
        Automatically assign color based on lyrical content and emotional tone.

        Args:
            text: The lyric text to analyze

        Returns:
            Rich color string for the text
        """
        lower_text = text.lower()

        # Emotional/intense phrases
        emotional_keywords = ["why not me", "do mi ti", "hurt", "pain", "cry", "broken"]
        if any(keyword in lower_text for keyword in emotional_keywords):
            return "bold bright_red"

        # Intimate/personal terms
        intimate_keywords = ["baby", "i know", "love", "heart", "kiss", "you"]
        if any(keyword in lower_text for keyword in intimate_keywords):
            return "bold yellow"

        # Questions or uncertainty
        if "?" in text or any(word in lower_text for word in ["why", "how", "what", "when"]):
            return "bold bright_magenta"

        # Default color for general lyrics
        return "bold cyan"

class SRTParser:
    """Handles parsing and processing of SRT subtitle files."""

    @staticmethod
    def parse_srt(filename: str) -> List[Tuple[float, str]]:
        """
        Parse an SRT file into timed lyric entries.

        Args:
            filename: Path to the SRT file

        Returns:
            List of tuples containing (start_time_seconds, text)

        Raises:
            FileNotFoundError: If the SRT file doesn't exist
            ValueError: If the SRT format is invalid
        """
        entries = []

        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read().split("\n\n")
        except FileNotFoundError:
            raise FileNotFoundError(f"SRT file '{filename}' not found")
        except Exception as e:
            raise ValueError(f"Error reading SRT file: {e}")

        for block in content:
            lines = block.strip().split("\n")

            if len(lines) >= 3:
                try:
                    # Parse timestamp (format: HH:MM:SS,mmm --> HH:MM:SS,mmm)
                    time_range = lines[1]
                    start_time_str = time_range.split(" --> ")[0]

                    # Convert to seconds
                    start_seconds = SRTParser._time_to_seconds(start_time_str)

                    # Extract text (may span multiple lines)
                    text = " ".join(lines[2:])
                    entries.append((start_seconds, text))

                except (IndexError, ValueError) as e:
                    console.print(f"[yellow]Warning: Skipping malformed entry: {e}[/yellow]")
                    continue

        if not entries:
            raise ValueError("No valid entries found in SRT file")

        return entries

    @staticmethod
    def _time_to_seconds(time_str: str) -> float:
        """
        Convert SRT timestamp to seconds.

        Args:
            time_str: Time string in format HH:MM:SS,mmm

        Returns:
            Time in seconds as float
        """
        try:
            # Split hours:minutes:seconds,milliseconds
            time_part, ms_part = time_str.split(',')
            hours, minutes, seconds = map(int, time_part.split(':'))
            milliseconds = int(ms_part)

            total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
            return total_seconds

        except ValueError as e:
            raise ValueError(f"Invalid time format '{time_str}': {e}")

def play_srt(filename: str, animator: Optional[LyricsAnimator] = None) -> None:
    """
    Play synchronized lyrics from an SRT file with animations.

    Args:
        filename: Path to the SRT file
        animator: Optional LyricsAnimator instance (creates new one if None)
    """
    if animator is None:
        animator = LyricsAnimator(console)

    try:
        # Parse the SRT file
        console.print(f"[blue]Loading lyrics from: {filename}[/blue]")
        lyrics = SRTParser.parse_srt(filename)
        console.print(f"[green]Loaded {len(lyrics)} lyric entries[/green]")

        # Display title panel
        title_panel = Panel(
            "[bold bright_white]🎵 Lyrics with Python 🎵[/bold bright_white]\n"
            f"[dim]Playing: {filename}[/dim]",
            border_style="bright_blue"
        )
        console.print(title_panel)
        console.print()

        # Start playback
        start_time = time.time()

        for start_seconds, text in lyrics:
            # Calculate timing
            current_time = time.time() - start_time

            if start_seconds > current_time:
                time.sleep(start_seconds - current_time)

            # Display lyric with effects if not empty
            if text.strip():
                color = animator.choose_color(text)
                animator.type_effect(
                    text, 
                    color=color, 
                    speed=0.08, 
                    glitch_speed=0.012
                )
                console.print()  # Add spacing between lines

        # End message
        console.print()
        console.print("[green]🎉 Lyrics complete! Thanks for watching! 🎉[/green]")

    except FileNotFoundError:
        console.print(f"[red]Error: SRT file '{filename}' not found[/red]")
    except ValueError as e:
        console.print(f"[red]Error parsing SRT file: {e}[/red]")
    except KeyboardInterrupt:
        console.print("\n[yellow]Playback interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")

def main():
    """Main entry point for the application."""
    try:
        # Initialize animator
        animator = LyricsAnimator(console)

        # Play the default song
        play_srt("WashingMachineHeart.srt", animator)

    except Exception as e:
        console.print(f"[red]Application error: {e}[/red]")

if __name__ == "__main__":
    main()
