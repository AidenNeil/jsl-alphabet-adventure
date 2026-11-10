# 🎯 NPM Commands Guide

## ✅ You Can Now Use NPM Commands!

I've created a `package.json` that wraps the Python commands, so you can use familiar npm commands:

---

## 🚀 **Available Commands:**

### **Start Development Server:**
```bash
npm run dev
```
**→ Runs:** `python app.py`
**→ Opens:** http://localhost:5000

### **Start Server (Alternative):**
```bash
npm start
```
**→ Same as** `npm run dev`

### **Run Demo:**
```bash
npm run demo
```
**→ Runs:** `python demo.py`
**→ Shows all features in console**

### **Run Tests:**
```bash
npm test
```
**→ Runs:** `python quick_test.py`
**→ Validates all modules**

### **Run Console Version:**
```bash
npm run console
```
**→ Runs:** `python main.py`
**→ Opens terminal version**

### **Install Dependencies:**
```bash
npm run install
```
**→ Runs:** `pip install -r requirements.txt`
**→ Installs Flask and dependencies**

---

## 📋 **Comparison:**

| Old (React/TypeScript) | New (Python/Flask) |
|------------------------|-------------------|
| `npm install` | `npm run install` or `pip install Flask` |
| `npm run dev` | `npm run dev` ✅ Same! |
| `npm start` | `npm start` ✅ Same! |
| Port 5173 | Port 5000 |
| Vite dev server | Flask dev server |

---

## 🎮 **Quick Start:**

```bash
# 1. Start the server
npm run dev

# 2. Open browser
# http://localhost:5000

# 3. Play and learn JSL!
```

---

## 🛑 **Stop Server:**
Press **CTRL + C** in the terminal

---

## 💡 **What's Different?**

### **Behind the Scenes:**
- `npm run dev` now calls `python app.py` instead of `vite`
- No build step needed
- Faster startup
- Same great experience!

### **Under the Hood:**
```json
{
  "scripts": {
    "dev": "python app.py",
    "start": "python app.py",
    "demo": "python demo.py",
    "test": "python quick_test.py",
    "console": "python main.py"
  }
}
```

---

## ✨ **Benefits:**

### **Familiar Workflow:**
- ✅ Use `npm run dev` like before
- ✅ Same commands, new technology
- ✅ No learning curve

### **Simpler Stack:**
- ✅ No build step
- ✅ No bundler configuration
- ✅ Pure Python + Flask
- ✅ Faster development

---

## 🌐 **Access the App:**

Once you run `npm run dev`, open:

# **http://localhost:5000**

---

## 📱 **Network Access:**

The server runs on all network interfaces, so you can access it from:

- **Local:** http://localhost:5000
- **Network:** http://YOUR-IP:5000
- **Example:** http://172.20.10.4:5000

---

## 🎊 **You're All Set!**

Use `npm run dev` just like you did before, but now it's powered by Python and Flask! 🐍⚡

---

## 📝 **Notes:**

- npm is only used as a task runner (convenience wrapper)
- The actual server is Python/Flask
- No node_modules folder needed
- No JavaScript bundling
- Just pure Python goodness!

Happy coding! 🚀
