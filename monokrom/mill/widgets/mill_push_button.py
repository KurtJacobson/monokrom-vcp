
from qtpy.QtWidgets import QPushButton


class MkMillPushButton(QPushButton):
    def __init__(self, parent=None):
        super(MkMillPushButton, self).__init__(parent)

        self.setText("MillPushButton")
