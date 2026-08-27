from __future__ import annotations
from phone.android import ANDROID

class TTSManager:
    def __init__(self, enabled=True, speech_rate=1.0, pitch=1.0, language="en"):
        self.enabled=enabled; self.speech_rate=speech_rate; self.pitch=pitch; self.language=language; self.engine=None
        if ANDROID:
            try:
                from jnius import autoclass, PythonJavaClass, java_method
                TextToSpeech=autoclass("android.speech.tts.TextToSpeech")
                Locale=autoclass("java.util.Locale")
                self.engine=TextToSpeech(__import__("phone.android",fromlist=["activity"]).activity(), None)
                self.engine.setSpeechRate(float(speech_rate)); self.engine.setPitch(float(pitch))
                self.engine.setLanguage(Locale.US if language.lower().startswith("en") else Locale.getDefault())
            except Exception: self.engine=None
    def speak(self,text):
        if not self.enabled or not text: return {"status":"disabled","message":"TTS is disabled."}
        if self.engine:
            try:
                self.engine.speak(text, 0, None, "NOVA")
                return {"status":"success","message":text}
            except Exception as exc: return {"status":"error","message":str(exc)}
        return {"status":"unsupported","message":"Android TTS is available in the Android build."}
