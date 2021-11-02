
import os

from qtpy.QtCore import Qt
from qtpy.QtCore import Slot, Property, Signal, QFile, QFileInfo, QDir, QIODevice, QModelIndex, QStringListModel
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QListView, QFileSystemModel, QFileIconProvider

from qtpyvcp.utilities.info import Info
from qtpyvcp.utilities.logger import getLogger
from qtpyvcp.widgets.dialogs import hideActiveDialog
from qtpyvcp.widgets.input_widgets.file_system import RemovableDeviceComboBox
from qtpyvcp.actions.program_actions import load as loadProgram

FILE_DIR = os.path.dirname(__file__)
ICON_DIR = os.path.join(FILE_DIR, '../icons')
FILE_ICON = os.path.join(ICON_DIR, 'file.png')
FOLDER_ICON = os.path.join(ICON_DIR, 'folder.png')
USB_ICON = os.path.join(ICON_DIR, 'usb.png')

LOG = getLogger(__name__)


class MkRemovableDeviceComboBox(RemovableDeviceComboBox):
    def __init__(self, parent=None):
        super(MkRemovableDeviceComboBox, self).__init__(parent)

    def onRemovableDevicesChanged(self, devices):

        self.blockSignals(True)

        self.clear()

        for label, path in self._file_locations.local_locations.items():
            self.addItem(label, {'path': os.path.expanduser(path)})

        self.insertSeparator(100)  # 100 so we are at end

        if devices:
            for devices_node, device_data in devices.items():
                self.addItem(QIcon(USB_ICON), device_data.get('label', 'Unknown'), device_data)

        self.blockSignals(False)


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


class MkFileSystemModel(QFileSystemModel):
    def __init__(self):
        super(MkFileSystemModel, self).__init__()

    def supportedDropActions(self):
        return Qt.CopyAction | Qt.MoveAction

    def flags(self, index):

        default_flags = QFileSystemModel.flags(self, index)

        if index.isValid():
            return Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | default_flags
        else:
            return Qt.ItemIsDropEnabled | default_flags

    def dropMimeData(self, data, action, row, column, index):

        if action == Qt.IgnoreAction:
            return True

        return True

    def setRootPath(self, path):
        super(MkFileSystemModel, self).setRootPath(path)
        if os.path.ismount(path):
            self.setFilter(QDir.AllDirs | QDir.AllEntries | QDir.NoDotAndDotDot)
        else:
            self.setFilter(QDir.AllDirs | QDir.AllEntries | QDir.NoDot)


class MkFileListView(QListView):

    rootChanged = Signal(str)

    def __init__(self, parent=None):
        super(MkFileListView, self).__init__(parent)

        self.info = Info()
        self.nc_file_editor = self.info.getEditor()
        self.nc_file_dir = self.info.getProgramPrefix()
        self.nc_file_exts = self.info.getProgramExtentions()

        # file system model
        self.model = MkFileSystemModel()
        # self.model.setReadOnly(True)
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
        self.clicked.connect(self.openLocation)
        self.activated.connect(self.openSelectedItem)

        self.model.rootPathChanged.connect(self.updateRootPath)

        self.setRootPath(os.path.expanduser('~/linuxcnc/nc_files'))

    def updateRootPath(self, root_path):
        self.setRootIndex(self.model.index(root_path))

    @Slot(str)
    def setRootPath(self, root_path):
        """Sets the currently displayed path."""

        # self.rootChanged.emit(root_path)
        self.model.setRootPath(root_path)
        self.setRootIndex(self.model.index(root_path))
        return True

    @Slot(QModelIndex)
    def openLocation(self, index):
        path = self.model.filePath(self.rootIndex())
        name = self.model.filePath(index)
        absolute_path = os.path.join(path, name)

        file_info = QFileInfo(absolute_path)
        if file_info.isDir():
            self.model.setRootPath(absolute_path)
            self.setRootIndex(self.model.index(absolute_path))
            self.rootChanged.emit(absolute_path)

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
                LOG.warn("Unsuported NC program type with extention .%s",
                         file_info.completeSuffix())
            hideActiveDialog()
            loadProgram(absolute_path)

    @Slot()
    def getSelection(self):
        """Returns list of selected indexes, or None."""
        selection = self.selection_model.selectedIndexes()
        if len(selection) == 0:
            return None
        return selection

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(MkFileListView, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            super(MkFileListView, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.MoveAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.copyFiles(links)
            # self.emit(QtCore.SIGNAL("dropped"), links)
        else:
            event.setDropAction(Qt.MoveAction)
            super(MkFileListView, self).dropEvent(event)

    def copyFiles(self, files):
        dst = self.model.filePath(self.rootIndex())

        for file in files:
            print(("Copy: {} > {}".format(file, dst)))
            self.copyRecursively(file, dst)

    def copyRecursively(self, src, tgt):
        src_info = QFileInfo(src)
        if src_info.isDir():
            tgt_dir = QDir(tgt)
            if not tgt_dir.mkdir(src_info.fileName()):
                return False
            src_dir = QDir(src)
            fnames = src_dir.entryList(QDir.Files | QDir.Dirs | QDir.NoDotAndDotDot | QDir.Hidden | QDir.System)
            for fname in fnames:
                new_src = os.path.join(src, fname)
                new_tgt = os.path.join(tgt, src_info.fileName())
                if not self.copyRecursively(new_src, new_tgt):
                    return False

        elif src_info.isFile():
            fname = src_info.fileName()
            if not QFile.copy(src, os.path.join(tgt, fname)):
                return False

        return True
