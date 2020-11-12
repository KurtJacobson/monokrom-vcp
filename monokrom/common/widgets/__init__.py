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

from mdi_entry import MkMdiEntry
class MkMdiEntry_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MkMdiEntry

from file_list_view import MkFileListView
class MkFileListView_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MkFileListView

from recent_file_list_view import MkRecentFileListView
class MkRecentFileListView_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MkRecentFileListView

from file_list_view import MkRemovableDeviceComboBox
class MkRemovableDeviceComboBox_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MkRemovableDeviceComboBox

from transparent_widget import MkTransparentWidget
class MkTransparentWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MkTransparentWidget
    def isContainer(self):
        return True

from group_box import MkGroupBox
class MkGroupBox_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MkGroupBox
    def isContainer(self):
        return True
    def domXml(self):
        return """<widget class="MkGroupBox" name="groupbox">
                  <property name="title">
                    <string>MkGroupBox</string>
                  </property>
                  </widget>"""

from tab_widget import MkTabWidget
class MkTabWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return MkTabWidget
    def isContainer(self):
        return True
    def domXml(self):
        return """<widget class="MkTabWidget" name="tabwidget">
                    <property name="geometry">
                     <rect>
                      <x>0</x>
                      <y>0</y>
                      <width>250</width>
                      <height>200</height>
                     </rect>
                    </property>
                    <widget class="QWidget" name="tab_1">
                     <attribute name="title">
                      <string>Page 1</string>
                     </attribute>
                    </widget>
                  </widget>"""