
from qtpy.QtWidgets import QLineEdit


class MkMillLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MkMillLineEdit, self).__init__(parent)

        self.setText("MillLineEdit")
