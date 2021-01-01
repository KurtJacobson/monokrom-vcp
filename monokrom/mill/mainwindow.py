
import linuxcnc

from qtpyvcp.plugins import getPlugin
from qtpyvcp.actions.machine_actions import setTaskMode

from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow


# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')

class MainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # connect widget signals
        self.mainModeTabWidget.currentChanged.connect(self.onModeTabIndexChanged)

        # connect status signals
        STATUS.task_mode.notify(self.onTaskModeChanged)
        STATUS.task_state.onValueChanged(self.onTaskStateChanged)
        STATUS.interp_state.notify(self.onInterpStateChanged)

    def onTaskStateChanged(self, task_state):
        self.mainModeTabWidget.setEnabled(task_state == linuxcnc.STATE_ON)

    def onModeTabIndexChanged(self, index):
        if index == 0:
            setTaskMode(linuxcnc.MODE_MANUAL)
        elif index == 1:
            setTaskMode(linuxcnc.MODE_MDI)
        else:
            setTaskMode(linuxcnc.MODE_AUTO)

    def onTaskModeChanged(self, task_mode):
        if task_mode == linuxcnc.MODE_MANUAL:
            self.mainModeTabWidget.setCurrentIndex(0)
        elif task_mode == linuxcnc.MODE_MDI:
            self.mainModeTabWidget.setCurrentIndex(1)
            self.programStackedWidget.setCurrentIndex(1)
        elif task_mode == linuxcnc.MODE_AUTO:
            self.mainModeTabWidget.setCurrentIndex(2)
            self.programStackedWidget.setCurrentIndex(0)

    def onInterpStateChanged(self, interp_state):
            if interp_state == linuxcnc.INTERP_IDLE:
                self.mainModeTabWidget.setTabEnabled(0, True)
                self.mainModeTabWidget.setTabEnabled(1, True)
            else:
                self.mainModeTabWidget.setTabEnabled(0, False)
                self.mainModeTabWidget.setTabEnabled(1, False)
