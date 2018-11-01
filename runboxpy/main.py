from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

Config.set('graphics', 'width', '620')
Config.set('graphics', 'height', '440')


class WelcomeScreen(Screen):
    pass


class RunBoxPySM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(WelcomeScreen(name="welcome"))


class RunBoxPyApp(App):
    def build(self):
        self.screen_manager = RunBoxPySM()
        return self.screen_manager


def main():
    return RunBoxPyApp().run()


if __name__ == '__main__':
    main()
