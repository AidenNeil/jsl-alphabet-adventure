# JSL Alphabet Adventure - Web Version

## 🌐 Run on the Web!

This is a Flask-based web application that runs in your browser, just like the original React app!

## 🚀 Quick Start

### 1. Install Flask
```bash
pip install Flask
```

### 2. Run the Web Server
```bash
python app.py
```

### 3. Open in Browser
Go to: **http://localhost:5000**

That's it! The application will open in your web browser.

## 📁 Web Version Structure

```
├── app.py                 # Flask web server
├── templates/             # HTML templates
│   ├── index.html         # Home page (mode selector)
│   ├── learn.html         # Learn mode page
│   └── quiz.html          # Quiz mode page (practice & challenge)
├── static/                # Static files
│   └── style.css          # Styling
└── src/assets/            # JSL letter images
```

## ✨ Features

### 🏠 **Home Page**
- Beautiful mode selection with animated cards
- Three game modes: Learn, Practice, Challenge

### 📖 **Learn Mode**
- Browse all 26 JSL letters
- Navigate with Previous/Next buttons or arrow keys
- Click any letter to jump directly to it
- Full descriptions and images for each sign

### ⚡ **Practice Mode**
- 10-question quiz
- 10 seconds per question
- Multiple choice (4 options)
- Real-time timer
- Score tracking
- Sound effects

### 🏆 **Challenge Mode**
- 10-question quiz
- 5 seconds per question (faster!)
- Multiple choice (4 options)
- Real-time timer
- Score tracking
- Sound effects

## 🎮 Controls

### Learn Mode
- **Next/Previous buttons**: Navigate through letters
- **Letter grid**: Click any letter to jump to it
- **Arrow keys**: Left/Right to navigate
- **Home button**: Return to mode selection

### Quiz Mode
- **Option buttons**: Click to answer
- **Timer**: Automatic timeout if time runs out
- **Exit button**: Return to mode selection

## 🎨 Features Preserved from Original

All features from the TypeScript/React version are preserved:
- ✅ Mode selection interface
- ✅ Learn mode with navigation
- ✅ Practice quiz (slow-paced)
- ✅ Challenge quiz (fast-paced)
- ✅ Timer system
- ✅ Score tracking
- ✅ Sound effects (Web Audio API)
- ✅ Responsive design
- ✅ Animations and transitions
- ✅ All 26 JSL letters with images

## 🔊 Sound Effects

The web version uses the Web Audio API for sound effects:
- ✅ Correct answer sound
- ✅ Incorrect answer sound
- ✅ Click sound
- ✅ Success celebration sound

## 📱 Responsive Design

The web app works on:
- 💻 Desktop browsers
- 📱 Mobile phones
- 📲 Tablets

## 🛠️ Technical Details

### Backend (Python/Flask)
- Flask web framework
- RESTful API endpoints
- Session management for quizzes
- Random question generation

### Frontend (HTML/CSS/JavaScript)
- Vanilla JavaScript (no framework needed)
- Modern CSS with gradients and animations
- Fetch API for backend communication
- Web Audio API for sounds

### API Endpoints
- `GET /` - Home page
- `GET /learn` - Learn mode page
- `GET /quiz/<mode>` - Quiz mode page
- `GET /api/alphabet` - Get all letters
- `GET /api/alphabet/<letter>` - Get specific letter
- `POST /api/quiz/start` - Start new quiz
- `GET /api/quiz/question/<session_id>` - Get current question
- `POST /api/quiz/answer` - Submit answer

## 🎯 Running on Different Ports

To run on a different port:
```python
# Edit app.py, change the last line:
app.run(debug=True, host='0.0.0.0', port=8080)  # Use port 8080
```

## 🌍 Running on Network

To access from other devices on your network:
1. Find your IP address (e.g., 192.168.1.100)
2. Run the app
3. Access from other devices: http://192.168.1.100:5000

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Try a different port
# Edit app.py and change port=5000 to port=5001
```

### Images Not Loading
- Make sure the `src/assets/` folder exists with all PNG files
- Check browser console for errors

### Flask Not Found
```bash
pip install Flask
```

## 📊 Comparison: Console vs Web

| Feature | Console Version | Web Version |
|---------|----------------|-------------|
| Interface | Text-based terminal | Browser with graphics |
| Images | File paths only | Full image display |
| Navigation | Keyboard input | Mouse + Keyboard |
| Sound | PyAudio (optional) | Web Audio API (built-in) |
| Platform | Any terminal | Any web browser |
| Installation | Python only | Python + Flask |

## 🎓 Educational Use

Perfect for:
- Learning JSL alphabet
- Classroom teaching
- Self-study
- Accessibility training
- Sign language practice

## 📝 Notes

- The web version does NOT require npm or Node.js
- Pure Python backend with Flask
- Lightweight and fast
- No database required (sessions stored in memory)
- All original functionality preserved

Enjoy learning JSL! 🤟
