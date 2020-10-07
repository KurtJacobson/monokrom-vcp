
from qtpy.QtWidgets import QGroupBox


class MkGroupBox(QGroupBox):
    def __init__(self, parent=None):
        super(MkGroupBox, self).__init__(parent)

    def resizeEvent(self, event):
        super(MkGroupBox, self).resizeEvent(event)
        qss = "::title {min-width: %ipx;}" % self.width()
        self.setStyleSheet(qss)
