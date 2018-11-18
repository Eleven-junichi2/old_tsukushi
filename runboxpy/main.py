# from pathlib import Path
import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.properties import \
    ObjectProperty
from kivy.core.text import LabelBase
from kivy.config import Config
# from filetreeview import FileTreeViewFileNode, FileTreeViewDirNode

# from uix.popup.filepopup import FolderChooserPopup

Config.set('graphics', 'width', f'{930}')
Config.set('graphics', 'height', f'{660}')

LabelBase.register("NotoSansCJKjp",
                   fn_regular="fonts/NotoSansCJKjp/NotoSansCJKjp-Regular.otf",
                   fn_bold="fonts/NotoSansCJKjp/NotoSansCJKjp-Bold.otf")


class ProjectLocationChooser(RelativeLayout):
    def __init__(self, chooser_user, **kwargs):
        super().__init__(**kwargs)
        self.chooser_user = chooser_user

    def is_dir(self, directory, filename):
        return os.path.isdir(os.path.join(directory, filename))

    def close_chooser_user(self, result=None):
        self.chooser_user.close(result)


class NewProjectScreen(Screen):
    new_project_name = ObjectProperty(None)
    project_location = ObjectProperty(None)

    # def choose_project_location(self):
    #     FolderChooserPopup(self.project_location, "text",
    #                        ProjectLocationChooser

    # def create_project(self):
    #     project_dir_location = Path(self.project_location.text)
    #     project_files_dir = project_dir_location / self.new_project_name.text
    #     if not os.path.exists(project_dir_location):
    #         os.mkdir(project_dir_location)
    #     if not os.path.exists(project_files_dir):
    #         os.mkdir(project_files_dir)


class WelcomeScreen(Screen):
    pass


class RunboxpySM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(WelcomeScreen(name="welcome"))
        self.add_widget(NewProjectScreen(name="new_project"))
        # self.add_widget(EditScreen(name="edit"))


class RunboxpyApp(App):
    def build(self):
        self.screen_manager = RunboxpySM()
        return self.screen_manager


def main():
    return RunboxpyApp().run()


if __name__ == '__main__':
    main()
