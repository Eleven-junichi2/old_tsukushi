from pathlib import Path

from kivy.uix.button import Button
from kivy.properties import (
    StringProperty, NumericProperty, ReferenceListProperty)
from kivy.lang import Builder

Builder.load_file(str(Path(__file__).parent / "button.kv"))


class IconButton(Button):
    icon = StringProperty("")
    padding_left = NumericProperty(0)
    padding_top = NumericProperty(0)
    padding_right = NumericProperty(0)
    padding_bottom = NumericProperty(0)
    padding = ReferenceListProperty(
        padding_left, padding_top, padding_right, padding_bottom)
