JSL Alphabet Adventure - Python Edition

An interactive application to learn and practice Jamaican Sign Language (JSL) alphabet.

## Features

- **Learn Mode**: Browse through all 26 JSL letters at your own pace
- **Practice Mode**: Test yourself with a slow-paced quiz (10 seconds per question)
- **Challenge Mode**: Fast-paced quiz to test your skills (5 seconds per question)
- **Sound Effects**: Audio feedback for correct/incorrect answers (requires PyAudio)
- **Progress Tracking**: Keep track of your learning progress

## Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Clone or download this repository

2. (Optional) Install PyAudio for sound effects:

   **Windows:**
   ```bash
   pip install pyaudio
   ```

   **Linux:**
   ```bash
   sudo apt-get install python3-pyaudio
   pip install pyaudio
   ```

   **macOS:**
   ```bash
   pip install pyaudio
   ```

   Note: The application will work without PyAudio, but sound effects will be disabled.

## Usage

### Run the Main Application

```bash
python main.py
```

This will start the interactive menu where you can choose between:
1. Learn Mode
2. Practice Mode
3. Challenge Mode

### Run Individual Modules

You can also run each mode independently for testing:

**Learn Mode:**
```bash
python learn_mode.py
```

**Practice Mode (slow):**
```bash
python quiz_mode.py
```

**Challenge Mode (fast):**
```bash
python quiz_mode.py --fast
```

**Mode Selector:**
```bash
python game_mode_selector.py
```

## Project Structure

```
.
├── main.py                 # Main application entry point
├── jsl_alphabet.py         # JSL alphabet data structure
├── game_mode_selector.py   # Mode selection interface
├── learn_mode.py           # Learn Mode implementation
├── quiz_mode.py            # Quiz Mode implementation (Practice & Challenge)
├── sound_effects.py        # Sound effects system
├── utils.py                # Utility functions
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── src/
    └── assets/            # JSL letter images
        ├── jsl-a.png
        ├── jsl-b.png
        └── ...
```

## Modules Overview

### `Jsl_alphabet.py`
Contains the JSL alphabet data structure with:
- Letter character
- Description of hand position
- Image file path

### `learn_mode.py`
Implements browsing functionality:
- Navigate through letters (next/previous)
- Jump to specific letter
- Display letter information

### `quiz_mode.py`
Implements quiz functionality:
- Random question generation
- Multiple choice options
- Timer system
- Score tracking
- Two difficulty levels

### `game_mode_selector.py`
Handles mode selection:
- Display available modes
- Mode switching
- Menu navigation

### `sound_effects.py`
Audio system using PyAudio:
- Correct answer sound
- Incorrect answer sound
- Click sound
- Success celebration sound

### `utils.py`
Utility functions:
- Input validation
- Screen clearing
- Formatting helpers
- User input handling

## Converted from TypeScript/React

This Python version was converted from a TypeScript/React web application. All core functionality has been preserved:

- ✅ All game modes (Learn, Practice, Challenge)
- ✅ JSL alphabet data with descriptions
- ✅ Quiz logic with timing and scoring
- ✅ Sound effects system
- ✅ Navigation and progress tracking

## Future Enhancements

Possible improvements:
- GUI version using Tkinter or Pygame
- Image display in terminal (using ASCII art or external viewer)
- Enhanced terminal UI with colors (using colorama or rich)
- Save/load progress
- Statistics tracking
- Leaderboard system

## License

This project contains JSL alphabet learning materials for educational purposes.

## Contributing

Feel free to contribute improvements or bug fixes!
