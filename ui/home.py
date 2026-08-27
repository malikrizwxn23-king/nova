from kivy.lang import Builder
from kivymd.app import MDApp
from core.ai_engine import AIEngine
from core.memory import Memory
from voice.speech import SpeechRecognizer, REQUEST_SPEECH
from voice.tts import TTSManager
from ui.theme import configure_theme
from phone.android import ANDROID

KV='''
Screen:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "14dp"
        MDTopAppBar:
            title: "NOVA"
        MDLabel:
            id: status
            text: "READY"
            halign: "center"
            size_hint_y: None
            height: "36dp"
        MDFloatingActionButton:
            icon: "microphone"
            pos_hint: {"center_x": .5}
            on_release: app.handle_listen()
        MDTextField:
            id: command_input
            hint_text: "Type a command"
            mode: "filled"
        MDRaisedButton:
            text: "SEND"
            pos_hint: {"center_x": .5}
            on_release: app.handle_send(command_input.text)
        MDCard:
            MDLabel:
                id: response_box
                text: "Hello, I am NOVA."
                padding: "12dp"
'''

class NovaApp(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs); self.ai_engine=AIEngine(); self.memory=Memory(); self.speech=SpeechRecognizer(); self.tts=TTSManager()
    def build(self): configure_theme(self); return Builder.load_string(KV)
    def _show(self,text,status="READY"):
        self.root.ids.response_box.text=text; self.root.ids.status.text=status
        if self.tts.enabled: self.tts.speak(text)
    def handle_send(self,text):
        if not text.strip(): return
        result=self.ai_engine.process(text); self.memory.add_history(text,result.text); self._show(result.text,result.status.upper())
    def handle_listen(self):
        if not ANDROID: self._show("Voice input works in the Android build.","ANDROID ONLY"); return
        self._show("Listening…","LISTENING"); self.speech.start_listening()
    def on_activity_result(self,request_code,result_code,data):
        if request_code==REQUEST_SPEECH and data:
            try:
                results=data.getStringArrayListExtra("android.speech.extra.RESULTS")
                if results and len(results): self.handle_send(str(results.get(0)))
            except Exception as exc: self._show(f"Speech error: {exc}","ERROR")

if __name__=="__main__": NovaApp().run()
