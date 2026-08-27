# NOVA v0.2.0

Free/local-first Android voice assistant built with Python + Kivy/KivyMD.

## What is implemented
- Offline command parser and safe command router
- Android app launching for common apps
- Android camera intent
- Android dialer (confirmation before call)
- WhatsApp compose flow (confirmation before message)
- Android timer/alarm intents
- Browser/web search intent
- Android volume/media hooks
- Battery/system information
- Android Text-to-Speech when available
- Android speech-recognition intent
- Local SQLite command history
- Explicit unsupported responses instead of fake success

## Important Android limitations
- Instagram/TikTok scrolling requires an Android AccessibilityService. This project deliberately does not pretend to have that permission; the commands return `unsupported` until a user-authorized AccessibilityService is added.
- Android background/always-on wake-word listening is OS/battery sensitive. The included service wrapper is only lifecycle scaffolding; it is not a hidden microphone recorder.
- Direct brightness changes can require the special Android `WRITE_SETTINGS` permission, so NOVA opens the appropriate system panel instead of silently claiming success.
- WhatsApp messages are opened in WhatsApp/browser compose flow; NOVA does not silently press Send.
- Calls open the dialer instead of silently placing a call.

## Desktop test
```bash
pip install -r requirements.txt
python -m pytest -q
python main.py
```

## Android build
On Linux/WSL with Buildozer configured:
```bash
buildozer android debug
```
The generated APK will be under `bin/`.
