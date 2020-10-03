from qtpy.QtWidgets import QGroupBox, QTabWidget

# patch QGroupBox so title expands to full width
def QGroupBox_resizeEvent(self, event):
    super(QGroupBox, self).resizeEvent(event)
    qss = "::title {min-width: %ipx;}" % self.width()
    self.setStyleSheet(qss)

QGroupBox.resizeEvent = QGroupBox_resizeEvent

# patch QTabWidget so tabs expand to full width
def QTabWidget_resizeEvent(self, event):
    super(QTabWidget, self).resizeEvent(event)
    qss = "::tab-bar {min-width: %ipx;}" % self.width()
    self.setStyleSheet(qss)

QTabWidget.resizeEvent = QTabWidget_resizeEvent
