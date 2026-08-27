from __future__ import annotations
from urllib.parse import quote_plus
from phone.android import ANDROID, Intent, Uri, start_activity

class BrowserManager:
    def open_url(self, url: str):
        if not url:
            return {"status": "error", "message": "No URL was provided."}
        if not ANDROID:
            return {"status": "unsupported", "message": "Browser control is available on Android builds."}
        try:
            start_activity(Intent(Intent.ACTION_VIEW, Uri.parse(url)))
            return {"status": "success", "message": f"Opening {url}."}
        except Exception as exc:
            return {"status": "error", "message": str(exc)}

    def search(self, query: str):
        if not query:
            return {"status": "error", "message": "No search query was provided."}
        return self.open_url("https://www.google.com/search?q=" + quote_plus(query))
