import os
from iniparse import INIConfig

from qtpy import uic
from qtpy.QtWidgets import QWidget, QListView

BASE_PATH = os.path.join(os.path.dirname(__file__))
CONFIG_DIR = os.environ.get('CONFIG_DIR', '/dev/null')
UI_FILE = os.path.join(os.path.dirname(__file__), "plasmac_run_settings.ui")

CONFIG_FILE = os.path.join('example_material.cfg')

print CONFIG_DIR


class PlasmaRunSettings(QWidget):
    def __init__(self, parent=None):
        super(PlasmaRunSettings, self).__init__(parent)

        uic.loadUi(UI_FILE, self)

        # self.readConfig(CONFIG_FILE)

    def readConfig(self, cfg_file):

        if not os.path.isfile(cfg_file):
            return

        with open(CONFIG_FILE, 'r') as fh:
            cfg = INIConfig(fh)

        for sec_name in sorted(cfg._sections):
            print sec_name
            section = getattr(cfg, sec_name)
            self.runMaterialComboBox.addItem(section.name, sec_name)