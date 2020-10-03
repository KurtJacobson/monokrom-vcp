from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from mk_line_edit import MyLineEdit
class MyLineEdit_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MyLineEdit

from mk_push_button import MyPushButton
class MkPushButton_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MyPushButton

from mk_dro import MonokromDroWidget, MonokromDroGroup
class MkDroWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MonokromDroWidget

class MkDroGroup_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MonokromDroGroup

from file_list_view import MkFileListView
class MkFileListView_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MkFileListView

from transparent_widget import MkTransparentWidget
class MkTransparentWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MkTransparentWidget
    def isContainer(self):
        return True
