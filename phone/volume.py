from __future__ import annotations
from phone.android import ANDROID, Context

class VolumeManager:
    def _adjust(self, direction):
        if not ANDROID:
            return {"status": "unsupported", "message": "Volume control is available on Android builds."}
        try:
            audio = __import__("phone.android", fromlist=["activity"]).activity().getSystemService(Context.AUDIO_SERVICE)
            stream = 3  # AudioManager.STREAM_MUSIC
            audio.adjustStreamVolume(stream, direction, 1)
            return {"status": "success", "message": "Volume changed."}
        except Exception as exc:
            return {"status": "error", "message": str(exc)}
    def increase(self): return self._adjust(1)
    def decrease(self): return self._adjust(-1)
    def mute(self): return self._adjust(-100)
    def unmute(self): return self._adjust(100)
