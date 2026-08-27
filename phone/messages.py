class MessageManager:
    """Handles drafting and sending messages via Android-supported flows."""

    def compose_message(self, contact: str, message: str = ""):
        if not contact:
            return {"status": "error", "message": "No contact was provided."}
        return {
            "status": "confirmation_required",
            "message": f"I prepared a message for {contact}. Please confirm before sending.",
            "content": message or "",
        }
