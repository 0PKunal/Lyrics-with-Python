import random
import time
from rich.console import Console

console = Console()
symbols = ['#', '$', '%', '&', '/', '!', '?', '@']

def type_effect(text, color="bold bright_white", speed=0.07, glitch_speed=0.012):
    """Typing + glitch effect for each lyric line"""
    display = [" "] * len(text)
    for i in range(len(text)):
        for _ in range(random.randint(2, 5)):  # glitch cycles
            display[i] = random.choice(symbols)
            console.print("".join(display), end="\r", style="bold magenta")
            time.sleep(glitch_speed)
        display[i] = text[i]
        console.print("".join(display), end="\r", style=color)
        time.sleep(speed)
    console.print("".join(display), style=color)

def parse_srt(filename):
    """Parses an .srt file into (start_time, text) entries"""
    entries = []
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().split("\n\n")
        for block in content:
            lines = block.strip().split("\n")
            if len(lines) >= 3:
                # Example: 00:00:05,000 --> 00:00:07,000
                time_range = lines[1]
                start = time_range.split(" --> ")[0]
                start_sec = (
                    int(start[0:2]) * 3600
                    + int(start[3:5]) * 60
                    + int(start[6:8])
                    + int(start[9:12]) / 1000
                )
                text = " ".join(lines[2:])
                entries.append((start_sec, text))
    return entries

def choose_color(text):
    """Automatically assign color based on lyric content"""
    lower = text.lower()
    if "why not me" in lower or "do mi ti" in lower:
        return "bold bright_red"
    elif "baby" in lower or "i know" in lower:
        return "bold yellow"
    else:
        return "bold cyan"

def play_srt(filename):
    lyrics = parse_srt(filename)
    t0 = time.time()
    for start_sec, text in lyrics:
        now = time.time() - t0
        if start_sec > now:
            time.sleep(start_sec - now)
        if text.strip():
            color = choose_color(text)
            type_effect(text, color=color, speed=0.08, glitch_speed=0.012)

if __name__ == "__main__":
    play_srt("WashingMachineHeart.srt")
