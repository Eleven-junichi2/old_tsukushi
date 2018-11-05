import traceback

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.config import Config

Config.set('graphics', 'width', '620')
Config.set('graphics', 'height', '440')


class BlockCodeBase:
    background_color = ListProperty([1, 1, 1, 1])
    border_color = ListProperty([1, 1, 1, 1])


class BlockCode(Widget):
    background_color = ListProperty([1, 1, 1, 1])
    border_color = ListProperty([1, 1, 1, 1])


class BlockFunction(BoxLayout, BlockCodeBase):
    function_name = ObjectProperty(None)
    argments = ObjectProperty(None)


class BlockVariable(BoxLayout, BlockCodeBase):
    variable_name = StringProperty("")
    value = StringProperty("")


class BlockScript(DragBehavior, BoxLayout):
    background_color = ListProperty([1, 1, 1, 1])
    border_color = ListProperty([1, 1, 1, 1])
    script_name = StringProperty("")
    code = StringProperty("")

    def add_block(self, block_chooser):
        if block_chooser.text == "print":
            block = BlockFunction()
            block.function_name.text = "print"
        elif block_chooser.text == "variable":
            block = BlockVariable()
        else:
            block = BlockCode()
        self.add_widget(block)

    def on_script_name(self, _, script_name):
        self.id = script_name

    def run_script(self):
        self.code = ""
        can_exec_code = False
        for child_widget in reversed(self.children):
            # Generate python code.
            if isinstance(child_widget, BlockFunction):
                self.code += "{}({})\n".format(
                    child_widget.function_name.text,
                    child_widget.argments.text)
                can_exec_code = True
            elif isinstance(child_widget, BlockVariable):
                self.code += "{} = {}\n".format(
                    child_widget.variable_name, child_widget.value)
                can_exec_code = True
        if can_exec_code:
            try:
                exec(self.code)
            except Exception:
                traceback.print_exc()


class IconButton(Button):
    icon = StringProperty("")


class EditScreen(Screen):
    block_code_area = ObjectProperty(None)

    def add_script(self):
        self.block_code_area.add_widget(BlockScript())


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
