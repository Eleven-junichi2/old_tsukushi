from pathlib import Path
import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.popup import Popup
from kivy.uix.treeview import TreeViewNode
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
    content = ObjectProperty(None)
    panel = ObjectProperty(None)
    label = ObjectProperty(None)

    def __init__(self, panel_opener, **kwargs):
        super().__init__(**kwargs)
        self.panel_opener = panel_opener

    def close_panel(self):
        self.panel_opener.open_flag = 0
        self.panel.remove_widget(self)
        self.content.clear_widgets()

    def rename_file(self, new_name):
        self.label.text = new_name


class EditArea(TabbedPanel):
    panels = ObjectProperty(None)

    def add_panel(self, opener, text=""):
        edit_panel_header = EditPanelHeader(opener)
        edit_panel = EditPanel()

        edit_panel_header.content = edit_panel
        edit_panel_header.label.text = text
        edit_panel_header.panel = self

        self.panels.add_widget(edit_panel)
        self.add_widget(edit_panel_header)
        opener.file_showner = edit_panel_header


class FileTreeViewNode(FloatLayout, TreeViewNode):
    file_name_input = ObjectProperty(None)
    treeview_user = ObjectProperty(None)

    def __init__(self, treeview_user, file_showner=None, **kwargs):
        super().__init__(**kwargs)
        self.treeview_user = treeview_user
        self.file_showner = file_showner
        self.open_flag = 0

    def select_node(self):
        self.open_flag += 1
        if self.open_flag < 2:
            self.treeview_user.select_node(self)

    def on_rename_file(self):
        self.treeview_user.rename_file(self.file_name_input.text)
        if self.file_showner:
            self.file_showner.rename_file(self.file_name_input.text)


class Editor(RelativeLayout):
    file_browser = ObjectProperty(None)
    edit_area = ObjectProperty(None)
    project_name = StringProperty("")
    project_dir = StringProperty("")

    def open_project(self, project_dir):
        self.project_dir = project_dir
        self.project_name = Path(self.project_dir).parts[-1]

    def select_node(self, node):
        print(f"odd: {node.odd}")
        print(f"is_selected: {node.is_selected}")
        self.edit_area.add_panel(node, node.file_name_input.text)

    def add_file_tree_node(self):
        file_tree_view_node = FileTreeViewNode(self)
        self.file_browser.add_node(file_tree_view_node)

    def add_file(self):
        self.add_file_tree_node()

    def rename_file(self, new_name):
        pass
        # self.edit_area.


class EditScreen(Screen):
    editor = ObjectProperty(None)


class NewProjectScreen(Screen):
    new_project_name = ObjectProperty(None)
    project_location = ObjectProperty(None)

    def create_project(self):
        project_dir_location = Path(self.project_location.text)
        project_files_dir = project_dir_location / self.new_project_name.text
        if not os.path.exists(project_dir_location):
            os.mkdir(project_dir_location)
        if not os.path.exists(project_files_dir):
            os.mkdir(project_files_dir)


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
