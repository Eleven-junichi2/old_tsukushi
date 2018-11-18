from kivy.uix.popup import Popup


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
