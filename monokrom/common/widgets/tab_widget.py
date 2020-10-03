
from qtpy.QtWidgets import QTabWidget


class MkTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MkTabWidget, self).__init__(parent)

    def resizeEvent(self, event):
        self.tabBar().setFixedWidth(event.size().width())
