# KeyboardFixer

A Windows Python utility that converts selected text typed with the wrong Arabic or English keyboard layout.

## What it does

- Converts selected text between Arabic and English keyboard layouts using a character mapping.
- Uses **Ctrl+B** as a global keyboard shortcut.
- Preserves whitespace when converting text.
- Runs with a system-tray icon; use **Exit** in the tray menu to stop it.

> **Note:** This is keyboard-layout conversion, not translation. It does not automatically detect intended language, and mixed or already-correct text may be converted unexpectedly. Select only text you intend to convert.

## Requirements

- Windows
- Python 3
- Dependencies in `requirements.txt`

## Run from source

```powershell
python -m pip install -r requirements.txt
python "text converter.py"
```

## Usage

1. Run the Python script.
2. Select the text that was typed with the wrong keyboard layout.
3. Press **Ctrl+B** to convert and replace the selected text.
4. To quit, use **Exit** from the system-tray icon.

## Limitations

- Requires a desktop environment where global keyboard shortcuts and clipboard operations work.
- Some apps may intercept keyboard shortcuts or restrict simulated copy/paste.
- The clipboard is changed during conversion; the previous clipboard content is not currently restored after a successful conversion.
- Conversion has not been validated here across all Arabic keyboard layouts and applications.

## Built with

Python, keyboard, pyperclip, pystray, Pillow.
