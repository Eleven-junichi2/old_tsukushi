from kivy.uix.floatlayout import FloatLayout
from kivy.uix.treeview import TreeViewNode
from kivy.properties import ObjectProperty


class FileTreeViewNode(FloatLayout, TreeViewNode):
    file_name_input = ObjectProperty(None)


class FileTreeViewFileNode(FileTreeViewNode):
    def __init__(self, treeview_user, file_showner=None, **kwargs):
        super().__init__(**kwargs)
        self.treeview_user = treeview_user
        self.file_showner = file_showner
        self.open_flag = 0
        self.file_name_input.bind(text=self.on_rename)

    def select_node(self):
        self.open_flag += 1
        if self.open_flag < 2:
            self.treeview_user.select_node(self)

    def on_rename(self, _, text):
        self.treeview_user.rename_file(text)
        if self.file_showner:
            self.file_showner.rename_file(text)


class FileTreeViewDirNode(FileTreeViewNode):
    def __init__(self, treeview_user, **kwargs):
        super().__init__(**kwargs)
        self.treeview_user = treeview_user
        self.is_leaf = False
        self.file_name_input.bind(text=self.on_rename)

    def on_rename(self, _, text):
        self.treeview_user.rename_dir(text)
