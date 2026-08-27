from __future__ import annotations
from phone.android import ANDROID, Intent, Uri, start_activity

class AppLauncher:
    """Launch common Android apps using explicit packages/intents."""
    KNOWN = {
        "whatsapp": "com.whatsapp",
        "instagram": "com.instagram.android",
        "youtube": "com.google.android.youtube",
        "chrome": "com.android.chrome",
        "tiktok": "com.zhiliaoapp.musically",
    }

    def get_installed_apps(self):
        return list(self.KNOWN)

    def launch(self, app_name: str):
        name = (app_name or "").strip().lower()
        if not name:
            return {"status": "error", "message": "No app name provided."}
        if not ANDROID:
            return {"status": "unsupported", "message": "App launching is available on Android builds."}
        package = self.KNOWN.get(name)
        try:
            if name == "settings":
                intent = Intent(Intent.ACTION_SETTINGS)
            else:
                pm = __import__("phone.android", fromlist=["activity"]).activity().getPackageManager()
                intent = pm.getLaunchIntentForPackage(package) if package else None
                if intent is None:
                    return {"status": "error", "message": f"{app_name} is not installed."}
            start_activity(intent)
            return {"status": "success", "message": f"Opening {app_name}."}
        except Exception as exc:
            return {"status": "error", "message": f"Could not open {app_name}: {exc}"}
