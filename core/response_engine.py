class ResponseEngine:
    """Builds user-friendly responses for intents and edge cases."""

    @staticmethod
    def build_response(intent_name: str, target: str | None = None, fallback: str = "I couldn't understand that request.") -> str:
        normalized = (intent_name or "").upper()
        if normalized == "GREETING":
            return "Hello, I'm NOVA. I'm ready to help."
        if normalized == "OPEN_APP":
            return f"Opening {target or 'the requested app'} now."
        if normalized == "MAKE_CALL":
            return f"Preparing to call {target or 'that contact'}."
        if normalized == "SEND_MESSAGE":
            return f"Preparing a message for {target or 'that contact'}."
        if normalized == "SET_TIMER":
            return f"Setting a timer for {target or 'the requested duration'}."
        if normalized == "SET_ALARM":
            return f"Setting an alarm for {target or 'the requested time'}."
        if normalized == "OPEN_CAMERA":
            return "Opening the camera for you."
        if normalized == "SHOW_DEVICE_INFO":
            return "Checking your device details."
        if normalized == "WEB_SEARCH":
            return f"Searching the web for {target or 'your query'}."
        return fallback
