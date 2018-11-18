from pathlib import Path

from kivy.uix.popup import Popup
from kivy.lang import Builder

from ..filechooser import SaveFileChooser, OpenFileChooser

Builder.load_file(str(Path(__file__).parent / "filepopup.kv"))


class SaveFilePopup(Popup):
    def __init__(self, file_chooser_user, **kwargs):
        super().__init__(**kwargs)
        self.content = SaveFileChooser()
        self.content.file_chooser_user = file_chooser_user


class OpenFilePopup(Popup):
    def __init__(self, file_chooser_user, **kwargs):
        super().__init__(**kwargs)
        self.content = OpenFileChooser()
        self.content.file_chooser_user = file_chooser_user


class FolderChooserPopup(Popup):
    def __init__(self, result_reciver, attr_name_to_assign_result: str,
                 file_browser, **kwargs):
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
