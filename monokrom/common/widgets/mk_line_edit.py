
from qtpy.QtWidgets import QLineEdit


class MyLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MyLineEdit, self).__init__(parent)

        self.setText("MyLineEdit")
