from pathlib import Path

from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file(str(Path(__file__).parent / "filechooser.kv"))


class SaveFileChooser(RelativeLayout):
    file_chooser = ObjectProperty(None)
    file_name_input = ObjectProperty(None)
    file_chooser_user = ObjectProperty(None)

    def close(self):
        self.file_chooser_user.close()

    def save(self, after_close=True):
        if self.file_name_input.text:
            self.file_chooser_user.save_file(file_chooser=self)
            if after_close:
                self.close()


class OpenFileChooser(RelativeLayout):
    file_chooser = ObjectProperty(None)
    file_chooser_user = ObjectProperty(None)

    def close(self):
        self.file_chooser_user.close()

    def open(self, after_close=True):
        if self.file_chooser.selection:
            self.file_chooser_user.open_file(file_chooser=self)
            if after_close:
                self.close()
