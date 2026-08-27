from __future__ import annotations
from phone.android import ANDROID, Intent, start_activity

class MediaController:
    def _key(self, code):
        if not ANDROID: return {"status":"unsupported","message":"Media control is available on Android builds."}
        try:
            intent = Intent(Intent.ACTION_MEDIA_BUTTON)
            # Sending key events directly varies by Android version; use media button broadcasts where permitted.
            key = __import__("phone.android", fromlist=["activity"]).activity().getSystemService("audio")
            key.dispatchMediaKeyEvent(__import__("phone.android", fromlist=["autoclass"]).autoclass("android.view.KeyEvent")(0, code))
            return {"status":"success","message":"Media command executed."}
        except Exception as exc: return {"status":"error","message":str(exc)}
    def play(self): return self._key(126)
    def pause(self): return self._key(127)
    def next_track(self): return self._key(87)
    def previous_track(self): return self._key(88)
