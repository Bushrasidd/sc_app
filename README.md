# Purrfect Screenshot App 🐾

A simple and cute screenshot saving application that automatically saves screenshots from your clipboard.

## Features

- 📸 Automatically saves screenshots from clipboard
- 🎯 Choose your own directory to save screenshots
- 🚫 Prevents duplicate screenshots using hash detection
- 🐱 Cute cat-themed interface
- ⚡ Runs in the background checking clipboard every 10 seconds

## How to Use

1. **Run the application** - Double-click `ScreenshotApp.exe` (or run `app.py` with Python)
2. **Choose directory** - Click "🐾 Choose Directory" to select where you want screenshots saved
3. **Copy screenshots** - Take screenshots (e.g., Windows + Shift + S) and copy them to clipboard
4. **Auto-save** - The app will automatically detect and save new screenshots to your chosen directory

The app will:
- Skip duplicate screenshots (won't save the same image twice)
- Save with timestamps: `sc2024-01-15_14-30-45.png`
- Create the directory if it doesn't exist

## Building from Source

### Requirements
- Python 3.x
- Required packages: `pillow`, `pyinstaller`

Install dependencies:
```bash
pip install pillow pyinstaller
```

### Build the EXE

1. Make sure you have `cat.ico` in the project directory
2. Run PyInstaller:
   ```bash
   python -m PyInstaller ScreenshotApp.spec
   ```
3. The executable will be created in the `dist` folder

### Run as Python Script

Simply run:
```bash
python app.py
```

## Notes

- The app checks the clipboard every 10 seconds
- Only new/unique screenshots are saved
- You can change the directory anytime by clicking "Choose Directory"
- Closing the window stops the app

## Files

- `app.py` - Main GUI application
- `main.py` - Core screenshot saving logic
- `cat.ico` - Application icon
- `ScreenshotApp.spec` - PyInstaller configuration

Enjoy capturing your screenshots! 🐾

