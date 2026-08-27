from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel


class SettingsScreen(MDScreen):
    """Settings screen skeleton for voice, AI, privacy, and permissions."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "settings"
        self.layout = MDBoxLayout(orientation="vertical", padding=20, spacing=12)
        self.layout.add_widget(MDLabel(text="Voice", font_style="H5"))
        self.layout.add_widget(MDLabel(text="TTS: On"))
        self.layout.add_widget(MDLabel(text="Speech rate: 1.0"))
        self.layout.add_widget(MDLabel(text="Privacy: local-only"))
        self.add_widget(self.layout)
