
import os

from qtpy.QtCore import Qt
from qtpy.QtCore import Slot, Property, Signal, QFile, QFileInfo, QDir, QIODevice
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QListView, QFileSystemModel, QFileIconProvider

from qtpyvcp.utilities.info import Info
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


class MkFileListView(QListView):

    rootChanged = Signal(str)

    def __init__(self, parent=None):
        super(MkFileListView, self).__init__(parent)

        self.info = Info()
        self.nc_file_editor = self.info.getEditor()
        self.nc_file_dir = self.info.getProgramPrefix()
        self.nc_file_exts = self.info.getProgramExtentions()

        # file system model
        self.model = QFileSystemModel()
        self.model.setReadOnly(True)
        self.model.setFilter(QDir.AllDirs | QDir.AllEntries | QDir.NoDot)
        self.setModel(self.model)

        # selection model
        self.selection_model = self.selectionModel()
        # self.selection_model.selectionChanged.connect(self.onSelectionChanged)

        # icon provider
        self.icon_provider = MkFileIconProvider()
        self.model.setIconProvider(self.icon_provider)

        # appearance
        self.setAlternatingRowColors(True)

        # signals
        self.activated.connect(self.openSelectedItem)
        self.clicked.connect(self.openSelectedItem)

        self.setRootPath(os.path.expanduser('~/linuxcnc/nc_files'))

    @Slot(str)
    def setRootPath(self, root_path):
        """Sets the currently displayed path."""

        # self.rootChanged.emit(root_path)
        self.model.setRootPath(root_path)
        self.setRootIndex(self.model.index(root_path))

        return True

    @Slot()
    def openSelectedItem(self, index=None):
        """If ngc file, opens in LinuxCNC, if dir displays dir."""
        if index is None:
            selection = self.getSelection()
            if selection is None:
                return
            index = selection[0]

        path = self.model.filePath(self.rootIndex())
        name = self.model.filePath(index)
        absolute_path = os.path.join(path, name)

        file_info = QFileInfo(absolute_path)
        if file_info.isDir():
            self.model.setRootPath(absolute_path)
            self.setRootIndex(self.model.index(absolute_path))
            self.rootChanged.emit(absolute_path)

        elif file_info.isFile():
            if file_info.completeSuffix() not in self.nc_file_exts:
                pass
                # LOG.warn("Unsuported NC program type with extention .%s",
                #          file_info.completeSuffix())
            loadProgram(absolute_path)

    @Slot()
    def getSelection(self):
        """Returns list of selected indexes, or None."""
        selection = self.selection_model.selectedIndexes()
        if len(selection) == 0:
            return None
        return selection