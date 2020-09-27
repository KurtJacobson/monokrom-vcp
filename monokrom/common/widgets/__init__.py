from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from mk_line_edit import MyLineEdit
class MyLineEdit_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MyLineEdit

from mk_push_button import MyPushButton
class MyPushButton_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MyPushButton

from mk_dro import MonokromDroWidget, MonokromDroGroup
class MonokromDroWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MonokromDroWidget

class MonokromDroGroup_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MonokromDroGroup

