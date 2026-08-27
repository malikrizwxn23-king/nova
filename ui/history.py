from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel


class HistoryScreen(MDScreen):
    """History screen showing recent commands and responses."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "history"
        self.layout = MDBoxLayout(orientation="vertical", padding=20, spacing=12)
        self.layout.add_widget(MDLabel(text="Command history", font_style="H5"))
        self.layout.add_widget(MDLabel(text="Open YouTube — Completed"))
        self.layout.add_widget(MDLabel(text="Set timer for 10 minutes — Completed"))
        self.add_widget(self.layout)
