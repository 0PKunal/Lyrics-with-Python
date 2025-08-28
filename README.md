# 🎵 Lyrics with Python

A dynamic, animated lyrics display application that brings songs to life in your terminal with stunning visual effects and synchronized timing.

## ✨ Features

- **Animated Typing Effects**: Watch lyrics appear character by character with realistic typing animations
- **Glitch Visual Effects**: Eye-catching glitch transitions using random symbols before revealing each character
- **Color-Coded Lyrics**: Intelligent color assignment based on lyrical content and emotional tone
- **SRT Subtitle Support**: Perfect synchronization using standard .srt subtitle files
- **Rich Terminal Output**: Beautiful, colorful display powered by the `rich` Python library

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- `rich` library for enhanced terminal output

### Setup
1. Clone this repository:
```bash
git clone https://github.com/0PKunal/Lyrics-with-Python.git
cd Lyrics-with-Python
```

2. Install required dependencies:
```bash
pip install rich
```

## 🎯 Usage

### Basic Usage
Run the default example with "Washing Machine Heart":
```bash
python WashingMachineHeart.py
```

### Custom Songs
To use your own lyrics:

1. **Create an SRT file** with your song lyrics in standard subtitle format:
```
1
00:00:09,063 --> 00:00:11,924
Your first lyric line

2
00:00:11,923 --> 00:00:16,085
Your second lyric line
```

2. **Modify the script** to use your SRT file:
```python
if __name__ == "__main__":
    play_srt("your_song.srt")
```

## 🎨 Customization

### Color Schemes
The application automatically assigns colors based on lyrical content:
- **Red**: Emotional or intense phrases (e.g., "why not me")
- **Yellow**: Intimate or personal terms (e.g., "baby", "I know")  
- **Cyan**: Default color for general lyrics

### Effect Parameters
Customize the visual effects by modifying these parameters in `type_effect()`:
- `speed`: Controls typing animation speed (default: 0.07)
- `glitch_speed`: Controls glitch effect duration (default: 0.012)
- `glitch_cycles`: Random range for glitch iterations (default: 2-5)

### Adding New Effects
The modular design makes it easy to add new visual effects:
```python
def your_custom_effect(text, **kwargs):
    # Your custom animation logic here
    pass
```

## 📁 Project Structure

```
Lyrics-with-Python/
├── WashingMachineHeart.py    # Main application script
├── WashingMachineHeart.srt   # Sample lyrics file
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── examples/                 # Additional example files
```

## 🛠️ Technical Details

### Core Functions
- `type_effect()`: Creates the animated typing with glitch effects
- `parse_srt()`: Parses SRT subtitle files into timed entries
- `choose_color()`: Intelligently assigns colors based on content
- `play_srt()`: Orchestrates the synchronized playback

### Dependencies
- **rich**: Advanced terminal formatting and colors
- **time**: Precise timing control for synchronization
- **random**: Glitch effect generation

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Add new songs**: Create SRT files for popular songs
2. **Improve effects**: Develop new visual animations
3. **Enhance colors**: Create smarter color-coding algorithms
4. **Add features**: GUI interface, audio synchronization, etc.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Thanks to the `rich` library developers for excellent terminal formatting
- Inspired by terminal-based music visualizers and lyric displays
- Sample song: "Washing Machine Heart" lyrics used for demonstration

## Help!

- **This README.md file is created by AI, it may have some mistakes**
- **Please contribute to improve it**

---

*Turn your terminal into a dynamic lyrics visualizer!* ✨


Made with ❤️ by [0PKunal](https://github.com/0PKunal)
