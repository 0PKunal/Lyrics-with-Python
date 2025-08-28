"""
Configuration file for Lyrics with Python
==========================================

Customize the visual effects, colors, and timing for your lyrics display.
"""

# Visual Effects Configuration
VISUAL_EFFECTS = {
    "typing_speed": 0.07,           # Seconds per character (lower = faster)
    "glitch_speed": 0.012,          # Speed of glitch effect
    "glitch_symbols": ['#', '$', '%', '&', '/', '!', '?', '@', '*', '+', '~', '^'],
    "min_glitch_cycles": 2,         # Minimum glitch iterations per character
    "max_glitch_cycles": 5,         # Maximum glitch iterations per character
}

# Color Themes
COLOR_THEMES = {
    "default": {
        "emotional": "bold bright_red",      # For emotional/intense phrases
        "intimate": "bold yellow",           # For personal/intimate terms
        "questions": "bold bright_magenta",  # For questions and uncertainty
        "general": "bold cyan",              # Default color for general lyrics
        "glitch": "bold magenta"             # Color for glitch effects
    },

    "neon": {
        "emotional": "bold bright_magenta",
        "intimate": "bold bright_yellow", 
        "questions": "bold bright_cyan",
        "general": "bold bright_green",
        "glitch": "bold bright_red"
    },

    "pastel": {
        "emotional": "bold red",
        "intimate": "bold yellow",
        "questions": "bold magenta", 
        "general": "bold blue",
        "glitch": "bold cyan"
    },

    "monochrome": {
        "emotional": "bold bright_white",
        "intimate": "bold white",
        "questions": "bold bright_white",
        "general": "bold white", 
        "glitch": "bold bright_white"
    }
}

# Keyword Categories for Auto-Color Assignment
KEYWORD_CATEGORIES = {
    "emotional": [
        "why not me", "do mi ti", "hurt", "pain", "cry", "broken", 
        "tears", "sad", "lonely", "miss", "sorry", "goodbye"
    ],

    "intimate": [
        "baby", "i know", "love", "heart", "kiss", "you", "together",
        "forever", "always", "mine", "yours", "hold", "close"
    ],

    "questions": [
        "why", "how", "what", "when", "where", "who", "should", "could", "would"
    ]
}

# Display Settings
DISPLAY_SETTINGS = {
    "show_title_panel": True,       # Show decorative title panel
    "add_line_spacing": True,       # Add extra spacing between lyrics
    "show_progress": True,          # Show loading progress
    "panel_border_style": "bright_blue"  # Border style for panels
}

# Advanced Settings
ADVANCED_SETTINGS = {
    "encoding": "utf-8",            # File encoding for SRT files
    "error_handling": "graceful",   # How to handle errors: "strict" or "graceful"
    "timing_precision": 0.01,       # Timing precision in seconds
}
