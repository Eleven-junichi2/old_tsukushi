import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.popup import Popup
from kivy.properties import (
    StringProperty, ObjectProperty, NumericProperty, ReferenceListProperty)
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


class ProjectLocationChooser(RelativeLayout):
    def __init__(self, chooser_user, **kwargs):
        super().__init__(**kwargs)
        self.chooser_user = chooser_user

    def is_dir(self, directory, filename):
        return os.path.isdir(os.path.join(directory, filename))

    def close_chooser_user(self, result=None):
        self.chooser_user.close(result)


class FolderChooserPopup(Popup):
    def __init__(self, result_reciver, attr_name_to_assign_result: str,
                 file_browser=ProjectLocationChooser, **kwargs):
        super().__init__(**kwargs)
        kwargs.pop("content", None)
        self.result_reciver = result_reciver
        self.attr_name_to_assign_result = attr_name_to_assign_result
        self.content = file_browser(self)

    def close(self, result=None):
        if result is not None:
            setattr(self.result_reciver, self.attr_name_to_assign_result,
                    result)
        self.dismiss()


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
