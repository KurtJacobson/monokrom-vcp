
from qtpy.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy
from qtpyvcp.widgets.base_widgets.base_widget import VCPBaseWidget
from qtpyvcp.widgets.input_widgets.mdientry_widget import MDIEntry


class MkMdiEntry(QWidget, VCPBaseWidget):
    def __init__(self, parent=None):
        super(MkMdiEntry, self).__init__(parent)

        self.label = QLabel("MDI", parent=self)
        self.mdi_entry = MDIEntry(parent=self)

        self.mdi_entry.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.mdi_entry)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)

        self.setLayout(hbox)
