from qtpy.QtWidgets import QGroupBox, QTabWidget, QWidget

# patch QGroupBox so title expands to full width
def QGroupBox_resizeEvent(self, event):
    super(QGroupBox, self).resizeEvent(event)
    qss = "::title {min-width: %ipx;}" % self.width()
    self.setStyleSheet(qss)

QGroupBox.resizeEvent = QGroupBox_resizeEvent
