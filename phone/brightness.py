from __future__ import annotations
from phone.android import ANDROID, Intent, start_activity

class BrightnessManager:
    def set(self, level: int | str = 50):
        try: value = int(level)
        except (TypeError, ValueError): return {"status":"error","message":"Brightness value was invalid."}
        if not 0 <= value <= 100: return {"status":"error","message":"Brightness must be between 0 and 100."}
        if not ANDROID: return {"status":"unsupported","message":"Brightness control is available on Android builds."}
        try:
            # Direct WRITE_SETTINGS is restricted; open the system panel when permission is not granted.
            start_activity(Intent("android.settings.action.MANAGE_WRITE_SETTINGS"))
            return {"status":"success","message":f"Android brightness settings opened. Set brightness to {value}%."}
        except Exception as exc: return {"status":"error","message":str(exc)}
