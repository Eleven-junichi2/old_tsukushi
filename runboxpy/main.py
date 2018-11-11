from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.properties import (
    StringProperty, ObjectProperty, NumericProperty, ReferenceListProperty)
# from kivy.garden.xpopup import XFileSave
from kivy.core.text import LabelBase
from kivy.config import Config

Config.set('graphics', 'width', f'{930}')
Config.set('graphics', 'height', f'{660}')

LabelBase.register("NotoSansCJKjp",
                   fn_regular="fonts/NotoSansCJKjp/NotoSansCJKjp-Regular.otf",
                   fn_bold="fonts/NotoSansCJKjp/NotoSansCJKjp-Bold.otf")


class IconButton(Button):
    icon = StringProperty("")
    padding_left = NumericProperty(0)
    padding_top = NumericProperty(0)
    padding_right = NumericProperty(0)
    padding_bottom = NumericProperty(0)
    padding = ReferenceListProperty(
        padding_left, padding_top, padding_right, padding_bottom)


class EditPanel(RelativeLayout):
    pass


class EditPanelHeader(TabbedPanelHeader):
    pass


class EditArea(TabbedPanel):
    panels = ObjectProperty(None)
    panel_headers = ObjectProperty(None)

    def add_panel(self):
        edit_panel_header = EditPanelHeader()
        edit_panel = EditPanel()
        edit_panel_header.content = edit_panel
        self.panels.add_widget(EditPanelHeader())
        self.add_widget(edit_panel_header)


class EditScreen(Screen):
    # code_input = ObjectProperty(None)
    def save(self):
        pass
        # home_dir = Path.home()
        # popup = XFileSave()


class NewProjectScreen(Screen):
    pass


class WelcomeScreen(Screen):
    pass


class RunboxpySM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(WelcomeScreen(name="welcome"))
        self.add_widget(NewProjectScreen(name="new_project"))
        self.add_widget(EditScreen(name="edit"))


class RunboxpyApp(App):
    def build(self):
        self.screen_manager = RunboxpySM()
        return self.screen_manager


def main():
    return RunboxpyApp().run()


if __name__ == '__main__':
    main()
