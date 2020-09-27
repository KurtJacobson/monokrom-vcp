
import os
from qtpy import uic
from qtpy.QtCore import Slot, Property
from qtpy.QtGui import QIcon, QPixmap
from qtpy.QtWidgets import QWidget, QVBoxLayout, QFrame

from qtpyvcp.plugins import getPlugin

BASE_PATH = os.path.join(os.path.dirname(__file__))
UI_FILE = os.path.join(os.path.dirname(__file__), "mk_dro.ui")

ICON_PATH = os.path.join(BASE_PATH, 'icons')

STATUS = getPlugin('status')


class MonokromDroWidget(QWidget):
    def __init__(self, parent=None, axis_number=None):
        super(MonokromDroWidget, self).__init__(parent)

        self._anum = 0
        self._aletter = 'x'
        self._style = ''
        self._homed = False

        uic.loadUi(UI_FILE, self)

        if axis_number is not None:
            self.axisNumber = axis_number

        STATUS.homed.notify(self.updateHomedStatus)

    @Property(int)
    def axisNumber(self):
        return self._anum

    @axisNumber.setter
    def axisNumber(self, axis):
        self._anum = max(0, min(axis, 8))
        self._aletter = 'xyzabcuvw'[self._anum]

        self.updateAxis()

    @Property(str)
    def styleClass(self):
        return self._style

    @styleClass.setter
    def styleClass(self, style):
        self._style = style
        self.ensurePolished()

    @Property(bool)
    def axisHomed(self):
        return self._homed

    @axisHomed.setter
    def axisHomed(self, homed):
        self._homed = homed
        for child in self.findChildren(QWidget):
            child.style().unpolish(child)
            child.style().polish(child)

    def updateAxis(self):
        self.dro_entry.axisNumber = self._anum
        self.axis_actions_button.setText(self._aletter.upper())

    def updateHomedStatus(self, homed):
        if homed[self._anum] == 1:
            self.homed_indicator.setPixmap(self.getPixmap('unhomed.png'))
            self.axisHomed = True
        else:
            self.homed_indicator.setPixmap(self.getPixmap('homed.png'))
            self.axisHomed = False

        # self.homed_indicator.style().unpolish(self.homed_indicator)
        # self.homed_indicator.style().polish(self.homed_indicator)

    def getIcon(self, name):
        # icon_name = 'axis-%(axis_letter).png' % {'axis_letter': self._anum}
        return QIcon(os.path.join(ICON_PATH, name))

    def getPixmap(self, name):
        return QPixmap(os.path.join(ICON_PATH, name))


class MonokromDroGroup(QWidget):
    def __init__(self, parent=None):
        super(MonokromDroGroup, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(8)
        self.layout.setContentsMargins(0, 0, 0, 0)

        axes = STATUS.axis_mask.getValue(format='list') or [0, 1, 3]

        for anum in axes:
            dro = MonokromDroWidget(self, anum)
            self.layout.addWidget(dro)

        self.setLayout(self.layout)
