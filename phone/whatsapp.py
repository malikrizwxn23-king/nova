from __future__ import annotations
from phone.android import ANDROID, Intent, Uri, start_activity

class WhatsAppManager:
    def open(self):
        if not ANDROID:
            return {"status": "unsupported", "message": "WhatsApp is available on Android builds."}
        try:
            intent = Intent(Intent.ACTION_VIEW, Uri.parse("whatsapp://send"))
            start_activity(intent)
            return {"status": "success", "message": "Opening WhatsApp."}
        except Exception as exc:
            return {"status": "error", "message": f"Could not open WhatsApp: {exc}"}

    def compose(self, contact: str, message: str = ""):
        if not contact:
            return {"status": "error", "message": "No contact was provided."}
        if not ANDROID:
            return {"status": "unsupported", "message": "WhatsApp messaging is available on Android builds."}
        try:
            uri = "https://wa.me/" + "".join(ch for ch in contact if ch.isdigit())
            if message:
                from urllib.parse import quote
                uri += "?text=" + quote(message)
            start_activity(Intent(Intent.ACTION_VIEW, Uri.parse(uri)))
            return {"status": "success", "message": f"WhatsApp compose opened for {contact}."}
        except Exception as exc:
            return {"status": "error", "message": f"Could not open WhatsApp: {exc}"}
