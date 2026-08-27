class AccessibilityBridge:
    """Optional Android accessibility abstraction for user-authorized UI actions."""

    def __init__(self, enabled: bool = False):
        self.enabled = enabled

    def status(self):
        return {"enabled": self.enabled, "message": "Accessibility is disabled." if not self.enabled else "Accessibility is enabled."}

    def click(self, target: str):
        if not self.enabled:
            return {"status": "error", "message": "Accessibility access is required to perform UI clicks."}
        return {"status": "success", "message": f"Clicking {target}."}

    def scroll(self):
        if not self.enabled:
            return {"status": "error", "message": "Accessibility access is required to scroll."}
        return {"status": "success", "message": "Scrolling the current screen."}
