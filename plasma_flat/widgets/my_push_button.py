
from qtpy.QtWidgets import QPushButton


class MyPushButton(QPushButton):
    def __init__(self, parent=None):
        super(MyPushButton, self).__init__(parent)

        self.setText("MyPushButton")
