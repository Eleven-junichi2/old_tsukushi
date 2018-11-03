from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, ListProperty
from kivy.config import Config

Config.set('graphics', 'width', '620')
Config.set('graphics', 'height', '440')


class BlockCode(DragBehavior, BoxLayout):
    background_color = ListProperty([1, 1, 1, 1])
    border_color = ListProperty([1, 1, 1, 1])


class IconButton(Button):
    icon = StringProperty("")


class EditScreen(Screen):
    pass


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
