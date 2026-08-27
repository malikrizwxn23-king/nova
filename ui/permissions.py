from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel


class PermissionsScreen(MDScreen):
    """Permission status display and guidance for Android access."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "permissions"
        self.layout = MDBoxLayout(orientation="vertical", padding=20, spacing=12)
        self.layout.add_widget(MDLabel(text="Permissions", font_style="H5"))
        self.layout.add_widget(MDLabel(text="Microphone: granted"))
        self.layout.add_widget(MDLabel(text="Camera: pending"))
        self.layout.add_widget(MDLabel(text="Phone: pending"))
        self.layout.add_widget(MDLabel(text="Notifications: optional"))
        self.add_widget(self.layout)
