from qtpy.QtWidgets import QGroupBox, QTabWidget

# patch QGroupBox so title expands to full width
def QGroupBox_resizeEvent(self, event):
    super(QGroupBox, self).resizeEvent(event)
    qss = "::title {min-width: %ipx;}" % self.width()
    self.setStyleSheet(qss)

QGroupBox.resizeEvent = QGroupBox_resizeEvent

# patch QTabWidget so tabs expand to full width
# FixMe: this is only needed on older versions of Qt,
# so we should only patch if needed.
def QTabWidget_resizeEvent(self, event):
    super(QTabWidget, self).resizeEvent(event)
    self.tabBar().setFixedWidth(self.width())

QTabWidget.resizeEvent = QTabWidget_resizeEvent
