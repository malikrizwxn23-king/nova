import re
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class ParsedIntent:
    raw_text: str; intent: str; target: Optional[str]=None; parameters: dict|None=None; confidence: float=0.0
    def to_dict(self): return asdict(self)

class IntentParser:
    """Offline parser for common NOVA commands."""
    def parse(self,text):
        cleaned=(text or "").strip(); low=cleaned.lower()
        if not cleaned: return ParsedIntent(text,"UNKNOWN",confidence=0)
        if ("hello" in low or "hi" in low) and "nova" in low: return ParsedIntent(cleaned,"GREETING",confidence=.95)
        if any(x in low for x in ("take photo","take a photo","take picture","take a picture")): return ParsedIntent(cleaned,"TAKE_PHOTO",confidence=.95)
        if "camera" in low: return ParsedIntent(cleaned,"OPEN_CAMERA",confidence=.92)
        if low.startswith(("open ","launch ")):
            t=self._extract_target(cleaned); return ParsedIntent(cleaned,"OPEN_APP",t,{"app_name":t},.9)
        if low.startswith("call ") or low.startswith("phone "):
            t=self._extract_target(cleaned); return ParsedIntent(cleaned,"MAKE_CALL",t,{"contact":t},.9)
        if "whatsapp" in low and ("message" in low or "msg" in low or "send" in low):
            t=self._extract_target(cleaned); return ParsedIntent(cleaned,"SEND_WHATSAPP",t,{"contact":t,"message":self._extract_message(cleaned)},.9)
        if low.startswith(("message ","msg ","send message ")):
            t=self._extract_target(cleaned); return ParsedIntent(cleaned,"SEND_MESSAGE",t,{"contact":t,"message":self._extract_message(cleaned)},.85)
        if "timer" in low: 
            d=self._duration(cleaned); return ParsedIntent(cleaned,"SET_TIMER",d,{"duration":d},.86)
        if "alarm" in low:
            t=self._time(cleaned); return ParsedIntent(cleaned,"SET_ALARM",t,{"time":t},.86)
        if "brightness" in low:
            m=re.search(r"(\d{1,3})",low); return ParsedIntent(cleaned,"SET_BRIGHTNESS",m.group(1) if m else None,{"level":m.group(1) if m else 50},.8)
        if "volume" in low:
            if any(x in low for x in ("down","decrease","lower")): i="VOLUME_DOWN"
            elif any(x in low for x in ("mute",)): i="MUTE"
            elif any(x in low for x in ("unmute",)): i="UNMUTE"
            else: i="VOLUME_UP"
            return ParsedIntent(cleaned,i,confidence=.8)
        if "next" in low and ("song" in low or "track" in low): return ParsedIntent(cleaned,"NEXT_TRACK",confidence=.8)
        if "previous" in low or "last song" in low: return ParsedIntent(cleaned,"PREVIOUS_TRACK",confidence=.8)
        if "pause" in low: return ParsedIntent(cleaned,"PAUSE",confidence=.8)
        if "play" in low or "music" in low: return ParsedIntent(cleaned,"PLAY",confidence=.8)
        if ("search" in low and "web" in low) or low.startswith("google "):
            q=self._search(cleaned); return ParsedIntent(cleaned,"WEB_SEARCH",q,{"query":q},.85)
        if "battery" in low or "device info" in low: return ParsedIntent(cleaned,"SHOW_DEVICE_INFO",confidence=.8)
        if "notification" in low: return ParsedIntent(cleaned,"SHOW_NOTIFICATIONS",confidence=.7)
        if "clear history" in low: return ParsedIntent(cleaned,"CLEAR_HISTORY",confidence=.95)
        if "settings" in low: return ParsedIntent(cleaned,"OPEN_SETTINGS",confidence=.8)
        if "scroll" in low and "instagram" in low: return ParsedIntent(cleaned,"SCROLL_INSTAGRAM",confidence=.85)
        if "scroll" in low and "tiktok" in low: return ParsedIntent(cleaned,"SCROLL_TIKTOK",confidence=.85)
        return ParsedIntent(cleaned,"UNKNOWN",confidence=.2)
    def _extract_target(self,text):
        m=re.search(r"(?:open|launch|call|phone|message|msg|send message|send)\s+(?:the\s+)?(.+?)(?:\s+(?:saying|that says|with message)\s+.+)?$",text,re.I); return m.group(1).strip().rstrip("?.") if m else None
    def _extract_message(self,text):
        m=re.search(r"(?:saying|that says|with message)\s+(.+)$",text,re.I); return m.group(1).strip().rstrip("?.") if m else ""
    def _duration(self,text):
        m=re.search(r"(\d+)\s*(seconds?|secs?|minutes?|mins?|hours?|hrs?)",text,re.I); return m.group(0) if m else None
    def _time(self,text):
        m=re.search(r"(\d{1,2}(?::\d{2})?\s*(?:am|pm))",text,re.I); return m.group(1) if m else None
    def _search(self,text):
        m=re.search(r"(?:search(?: the web)? for|google)\s+(.+)",text,re.I); return m.group(1).strip().rstrip("?.") if m else ""
