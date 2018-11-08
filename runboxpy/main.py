import traceback

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty
from kivy.config import Config

Config.set('graphics', 'width', '620')
Config.set('graphics', 'height', '440')


class IconButton(Button):
    icon = StringProperty("")


class EditScreen(Screen):
    code_input = ObjectProperty(None)

    def run_code(self):
        try:
            exec(self.code_input.text)
        except Exception:
            traceback.print_exc()


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
