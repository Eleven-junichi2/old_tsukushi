from pathlib import Path
import os
import sys

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
from kivy.config import Config

from .projectmanager import ProjectMaker, Project
from .uix.popup.filepopup import SaveFilePopup, OpenFilePopup
from .uix.button import IconButton

Config.set('graphics', 'width', f'{930}')
Config.set('graphics', 'height', f'{660}')

SCRIPT_DIR = Path(__file__).parent
print(SCRIPT_DIR)

LabelBase.register("NotoSansCJKjp",
                   fn_regular=str(
                       SCRIPT_DIR /
                       "fonts/NotoSansCJKjp/NotoSansCJKjp-Regular.otf"),
                   fn_bold=str(
                       SCRIPT_DIR /
                       "fonts/NotoSansCJKjp/NotoSansCJKjp-Bold.otf"))


class IconButton(IconButton):
    pass


class ProjectLocationChooser(RelativeLayout):
    def __init__(self, chooser_user, **kwargs):
        super().__init__(**kwargs)
        self.chooser_user = chooser_user

    def is_dir(self, directory, filename):
        return os.path.isdir(os.path.join(directory, filename))

    def close_chooser_user(self, result=None):
        self.chooser_user.close(result)


class EditScreen(Screen):
    text_input = ObjectProperty(None)

    def open_project(self, project: Project):
        """
        Args:
            project (Project): A project object.
        """
        self.project = project

    def show_save_file(self):
        popup = SaveFilePopup(self)
        popup.content.file_chooser.path = str(self.project.files_location)
        popup.content.close = popup.dismiss
        popup.open()

    def save_file(self, file_chooser):
        save_location = (Path(file_chooser.file_chooser.path) /
                         file_chooser.file_name_input.text)
        with open(str(save_location), "w") as file:
            file.write(self.text_input.text)

    def show_open_file(self):
        popup = OpenFilePopup(self)
        popup.content.file_chooser.path = str(self.project.files_location)
        popup.content.close = popup.dismiss
        popup.open()

    def open_file(self, file_chooser):
        with open(file_chooser.file_chooser.selection[0], "r") as file:
            self.text_input.text = file.read()


class NewProjectScreen(Screen):
    new_project_name = ObjectProperty(None)
    project_location = ObjectProperty(None)

    def create_project(self):
        project_dir_location = Path(self.project_location.text)
        project_maker = ProjectMaker(project_dir_location)
        return project_maker.generate_project(self.new_project_name.text)


class WelcomeScreen(Screen):
    pass


class LicenseScreen(Screen):
    pass


class TsukushiSM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(WelcomeScreen(name="welcome"))
        self.add_widget(LicenseScreen(name="license"))
        self.add_widget(NewProjectScreen(name="new_project"))
        self.add_widget(EditScreen(name="edit"))


class TsukushiApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.script_parent_dir = SCRIPT_DIR
        self.icon = str(SCRIPT_DIR / "images/icon.png")

    def build(self):
        self.screen_manager = TsukushiSM()
        return self.screen_manager


def main():
    return TsukushiApp().run()


if __name__ == '__main__':
    if hasattr(sys, "_MEIPASS"):
        resource_add_path(sys._MEIPASS)
    main()
