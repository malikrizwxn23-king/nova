class WakeWordEngine:
    def __init__(self,wake_word="NOVA"): self.wake_word=wake_word; self.enabled=False
    def start(self): self.enabled=True; return True
    def stop(self): self.enabled=False; return True
    def detect(self,text=None): return bool(self.enabled and text and self.wake_word.lower() in text.lower())
