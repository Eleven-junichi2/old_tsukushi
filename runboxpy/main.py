from pathlib import Path
import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.properties import StringProperty
# from kivy.garden.xpopup import XFileSave
# from kivy.core.text import LabelBase
from kivy.config import Config

Config.set('graphics', 'width', '620')
Config.set('graphics', 'height', '440')

fonts_dir_path = Path(__file__) / Path("./fonts/")
print(f"testtest: {fonts_dir_path.exists()}")
# for font_dir in os.listdir(fonts_dir):
    # for font_name in font_dir:
        # print(font_dir, font_name)
        # LabelBase.register(font_name, fn_bold=font_name)


class IconButton(Button):
    icon = StringProperty("")


class EditPanel(TabbedPanelItem):
    pass


class EditArea(TabbedPanel):
    def add_panel(self):
        self.add_widget(EditPanel())


class EditScreen(Screen):
    # code_input = ObjectProperty(None)
    def save(self):
        pass
        # home_dir = Path.home()
        # popup = XFileSave()


class WelcomeScreen(Screen):
    pass


class RunboxpySM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(WelcomeScreen(name="welcome"))
        self.add_widget(EditScreen(name="edit"))


class RunboxpyApp(App):
    def build(self):
        self.screen_manager = RunboxpySM()
        return self.screen_manager


def main():
    return RunboxpyApp().run()


if __name__ == '__main__':
    main()
