from __future__ import annotations
from phone.android import ANDROID, Intent, start_activity_for_result

REQUEST_SPEECH=4201

class SpeechRecognizer:
    def __init__(self): self.is_listening=False
    def start_listening(self):
        if not ANDROID: return False
        try:
            intent=Intent("android.speech.action.RECOGNIZE_SPEECH")
            intent.putExtra("android.speech.extra.LANGUAGE_MODEL","free_form")
            intent.putExtra("android.speech.extra.PROMPT","Speak to NOVA")
            start_activity_for_result(intent, REQUEST_SPEECH); self.is_listening=True; return True
        except Exception: return False
    def stop_listening(self): self.is_listening=False; return True
    def recognize(self,text=None): return text or ""
    def handle_error(self,error_message="Speech recognition failed."): return {"status":"error","message":error_message}
