class ContactManager:
    """Contact lookup abstraction."""

    def find_contact(self, name: str):
        if not name:
            return {"status": "error", "message": "No name specified."}
        return {"status": "success", "contact": name}
