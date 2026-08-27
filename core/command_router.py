from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Optional
from core.security import Security
from phone.apps import AppLauncher
from phone.camera import CameraManager
from phone.calls import CallManager
from phone.whatsapp import WhatsAppManager
from phone.alarms import AlarmManager
from phone.browser import BrowserManager
from phone.volume import VolumeManager
from phone.brightness import BrightnessManager
from phone.media import MediaController
from phone.device import DeviceInfo

@dataclass
class CommandResult:
    intent:str; status:str; message:str; target:Optional[str]=None; parameters:dict[str,Any]=field(default_factory=dict)

class CommandRouter:
    def __init__(self):
        self.apps=AppLauncher(); self.camera=CameraManager(); self.calls=CallManager(); self.whatsapp=WhatsAppManager(); self.alarms=AlarmManager(); self.browser=BrowserManager(); self.volume=VolumeManager(); self.brightness=BrightnessManager(); self.media=MediaController()
    def execute(self,intent_name,target=None,parameters=None,confirmed=False):
        intent=(intent_name or "UNKNOWN").upper(); p=parameters or {}; t=target
        if Security.requires_confirmation(intent) and not confirmed:
            return CommandResult(intent,"confirmation_required",Security.confirmation_message(intent),t,p)
        if intent=="GREETING": return CommandResult(intent,"success","Hello, I am NOVA. I am ready.",t,p)
        if intent=="OPEN_APP": r=self.apps.launch(t or p.get("app_name"))
        elif intent in {"OPEN_CAMERA","TAKE_PHOTO"}: r=self.camera.open_camera()
        elif intent=="MAKE_CALL": r=self.calls.call(t or p.get("contact"))
        elif intent in {"SEND_WHATSAPP","SEND_MESSAGE"}: r=self.whatsapp.compose(t or p.get("contact"),p.get("message", ""))
        elif intent=="SET_TIMER": r=self.alarms.set_timer(t or p.get("duration"))
        elif intent=="SET_ALARM": r=self.alarms.set_alarm(t or p.get("time"))
        elif intent=="WEB_SEARCH": r=self.browser.search(t or p.get("query"))
        elif intent=="VOLUME_UP": r=self.volume.increase()
        elif intent=="VOLUME_DOWN": r=self.volume.decrease()
        elif intent=="MUTE": r=self.volume.mute()
        elif intent=="UNMUTE": r=self.volume.unmute()
        elif intent=="SET_BRIGHTNESS": r=self.brightness.set(p.get("level",50))
        elif intent=="PLAY": r=self.media.play()
        elif intent=="PAUSE": r=self.media.pause()
        elif intent=="NEXT_TRACK": r=self.media.next_track()
        elif intent=="PREVIOUS_TRACK": r=self.media.previous_track()
        elif intent=="SHOW_DEVICE_INFO": r=DeviceInfo.get_system_info(); r={"status":r["status"],"message":str(r)}
        elif intent in {"SCROLL_INSTAGRAM","SCROLL_TIKTOK"}: r={"status":"unsupported","message":"Scrolling requires a user-enabled Android AccessibilityService; NOVA does not fake this action."}
        elif intent=="CLEAR_HISTORY": r={"status":"success","message":"History clear requested."}
        elif intent=="OPEN_SETTINGS": r={"status":"success","message":"Use Android settings from the NOVA permissions screen."}
        else: return CommandResult(intent,"unknown","I couldn't understand that command.",t,p)
        return CommandResult(intent,r.get("status","error"),r.get("message",str(r)),t,p)
