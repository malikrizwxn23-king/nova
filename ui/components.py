from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton, MDRaisedButton


Builder.load_string(
    '''
    <PulseCircle@MDCard>:
        size_hint: None, None
        size: "110dp", "110dp"
        radius: [55, 55, 55, 55]
        md_bg_color: app.theme_cls.primary_color
        elevation: 6

        MDLabel:
            text: "NOVA"
            halign: "center"
            valign: "middle"
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
    '''
)


class PulseCircle(MDCard):
    pulse_value = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animation = Animation(pulse_value=2, duration=1.5) + Animation(pulse_value=1, duration=1.5)
        self.animation.repeat = True
        self.animation.start(self)

    def on_pulse_value(self, instance, value):
        self.scale = value
