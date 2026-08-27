from __future__ import annotations
from phone.android import ANDROID

class NovaService:
    """Lifecycle wrapper. A true Android foreground Service needs a native service entry."""
    def __init__(self): self.running=False
    def start(self): self.running=True; return {"status":"success","message":"NOVA service started."}
    def stop(self): self.running=False; return {"status":"success","message":"NOVA service stopped."}
