
import os

from qtpy.QtCore import Qt, Slot, Property, Signal, QFile
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QListWidget, QFileIconProvider, QListWidgetItem

from qtpyvcp.utilities.info import Info
from qtpyvcp.plugins import getPlugin
from qtpyvcp.widgets.dialogs import hideActiveDialog
from qtpyvcp.actions.program_actions import load as loadProgram

FILE_DIR = os.path.dirname(__file__)
ICON_DIR = os.path.join(FILE_DIR, '../icons')
FILE_ICON = os.path.join(ICON_DIR, 'file.png')
FOLDER_ICON = os.path.join(ICON_DIR, 'folder.png')


class MkFileIconProvider(QFileIconProvider):
    def __init__(self):
        super(MkFileIconProvider, self).__init__()

    @Slot(QFileIconProvider.IconType)
    def icon(self, icon_type):
        if icon_type == QFileIconProvider.Folder:
            return QIcon(FOLDER_ICON)
        elif icon_type == QFileIconProvider.File:
            return QIcon(FILE_ICON)
        else:
            return QIcon()


class MkRecentFileListView(QListWidget):

    rootChanged = Signal(str)

    def __init__(self, parent=None):
        super(MkRecentFileListView, self).__init__(parent)

        self.status = getPlugin('status')

        self.update(self.status.recent_files())
        self.status.recent_files.notify(self.update)

        self.itemActivated.connect(self.openSelected)

    @Slot()
    def openSelected(self):
        try:
            item = self.selectedItems()[0]
            fpath = item.data(Qt.UserRole)
            loadProgram(fpath)
            hideActiveDialog()
        except (IndexError, AttributeError):
            pass

    @Slot()
    def removeSelected(self):
        try:
            item = self.selectedItems()[0]
            fpath = item.data(Qt.UserRole)
            recents = self.status.recent_files.getValue()
            recents.remove(fpath)
            self.status.recent_files.setValue(recents)
        except (ValueError, IndexError):
            pass

    def update(self, files):
        self.clear()
        for i, fname in enumerate(files):
            text = os.path.basename(fname)
            icon = QIcon(FILE_ICON)
            item = QListWidgetItem(icon, text)
            item.setData(Qt.UserRole, fname)
            self.addItem(item)
