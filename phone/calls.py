from __future__ import annotations
from phone.android import ANDROID, Intent, Uri, start_activity

class CallManager:
    """Uses the Android dialer so NOVA never silently places a call."""
    def call(self, target: str):
        target = (target or "").strip()
        if not target:
            return {"status": "error", "message": "No contact or number was provided."}
        if not ANDROID:
            return {"status": "unsupported", "message": "Calling is available on Android builds."}
        try:
            intent = Intent(Intent.ACTION_DIAL, Uri.parse("tel:" + target))
            start_activity(intent)
            return {"status": "success", "message": f"Dialer opened for {target}."}
        except Exception as exc:
            return {"status": "error", "message": f"Could not open dialer: {exc}"}
