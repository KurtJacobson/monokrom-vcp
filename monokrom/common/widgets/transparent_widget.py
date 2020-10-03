
from qtpy.QtGui import QPainter, QColor
from qtpy.QtWidgets import QWidget


class MkTransparentWidget(QWidget):
    def __init__(self, parent=None):
        super(MkTransparentWidget, self).__init__(parent)

        self.bg_color = QColor(22, 22, 14, 0)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(self.rect(), self.bg_color)
        qp.end()
