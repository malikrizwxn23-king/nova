class NotificationManager:
    """Local notification summary without secret external transmission."""

    def count(self):
        return {"status": "success", "count": 0, "message": "You have no new notifications."}

    def summarize(self):
        return {"status": "success", "summary": "No notifications found."}
