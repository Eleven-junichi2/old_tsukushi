from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex

<SaveFileChooser>:
    file_chooser: file_chooser
    file_name_input: file_name_input
    BoxLayout:
        orientation: 'vertical'
        TextInput:
            text: file_chooser.path
            size_hint_y: None
            height: self.minimum_height
            multiline: False
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            Button:
                text: "Icon View"
                size_hint_y: None
                height: self.texture_size[1]
                on_release: file_chooser.view_mode = 'icon'
            Button:
                text: "List View"
                size_hint_y: None
                height: self.texture_size[1]
                on_release: file_chooser.view_mode = 'list'
        FileChooser:
            id: file_chooser
            FileChooserIconLayout
            FileChooserListLayout
        BoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: self.minimum_height
            TextInput:
                id: file_name_input
                hint_text: "file name"
                size_hint_y: None
                height: self.minimum_height
                multiline: False
            Button:
                text: "Save"
                size_hint_x: 0.2
                size_hint_y: None
                height: file_name_input.height
                on_release:
                    root.save()
            Button:
                text: "Cancel"
                size_hint_x: 0.1
                size_hint_y: None
                width: self.texture_size[0] * 1.5
                height: file_name_input.height
                on_release: root.close()

<OpenFileChooser>:
    file_chooser: file_chooser
    BoxLayout:
        orientation: 'vertical'
        TextInput:
            text: file_chooser.path
            size_hint_y: None
            height: self.minimum_height
            multiline: False
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            Button:
                text: "Icon View"
                size_hint_y: None
                height: self.texture_size[1]
                on_release: file_chooser.view_mode = 'icon'
            Button:
                text: "List View"
                size_hint_y: None
                height: self.texture_size[1]
                on_release: file_chooser.view_mode = 'list'
        FileChooser:
            id: file_chooser
            FileChooserIconLayout
            FileChooserListLayout
        BoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: open_button.texture_size[1] * 1.5
            Button:
                id: open_button
                text: "Open"
                on_release:
                    root.open()
            Button:
                text: "Cancel"
                size_hint_x: 0.2
                on_release: root.close()
""")


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
