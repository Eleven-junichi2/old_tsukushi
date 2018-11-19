from kivy.uix.button import Button
from kivy.properties import (
    StringProperty, NumericProperty, ReferenceListProperty)
from kivy.lang import Builder

Builder.load_string("""
<IconButton>:
    Widget:
        pos: self.parent.pos
        size: self.parent.size
        canvas.before:
            Rectangle:
                source: root.icon
                pos: self.x + root.padding_left, self.y + root.padding_bottom
                size:
                    self.width - root.padding_right * 2, self.height -\\
                    root.padding_top * 2
""")


class IconButton(Button):
    icon = StringProperty("")
    padding_left = NumericProperty(0)
    padding_top = NumericProperty(0)
    padding_right = NumericProperty(0)
    padding_bottom = NumericProperty(0)
    padding = ReferenceListProperty(
        padding_left, padding_top, padding_right, padding_bottom)
