
import os
import inspect

from iniparse import INIConfig

from qtpyvcp.plugins import DataPlugin
from qtpyvcp.utilities.logger import getLogger
from qtpyvcp.utilities.settings import addSetting, setting, Setting

LOG = getLogger('qtpyvcp.' + __name__)

CONFIG_DIR = os.environ.get('CONFIG_DIR', '/dev/null')
UI_FILE = os.path.join(os.path.dirname(__file__), "plasmac_run_settings.ui")

CONFIG_FILE = os.path.join('example_material.cfg')


def isSetting(obj):
    return isinstance(obj, Setting)


class MaterialSettings(DataPlugin):
    def __init__(self):
        super(MaterialSettings, self).__init__()

        self._ini_config = None
        self._material = None
        self._materials = []

        self._settings = {name: obj for name, obj in
                            inspect.getmembers(self, isSetting)}

    # def initialise(self):
        self.readMaterialConfig(CONFIG_FILE)

    def readMaterialConfig(self, cfg_file):

        if not os.path.isfile(cfg_file):
            return

        with open(CONFIG_FILE, 'r') as fh:
            self._ini_config = INIConfig(fh)

        # print sorted(self._ini_config._sections)[0]
        self._material = self._ini_config[sorted(self._ini_config._sections)[0]]

        for setting_name, setting_obj in self._settings.items():
            print setting_name
            value = self._material[setting_name]
            setting_obj.setValue(value)


    @setting("plasmac.material.kerf_width",
             default_value=1.5,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def kerf_width(self, obj):
        return obj.normalizeValue(self._material.kerf_width)

    @kerf_width.setter
    def kerf_width(self, obj, kerf_width):
        new_val = obj.normalizeValue(kerf_width)
        LOG.error("PlasmaC Kerf Width changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)

    @setting("plasmac.material.pierce_height",
             default_value=1.0,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def pierce_height(self, obj):
        return obj.normalizeValue(self._material.pierce_height)

    @pierce_height.setter
    def pierce_height(self, obj, pierce_height):
        new_val = obj.normalizeValue(pierce_height)
        LOG.error("PlasmaC Pierce Height changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)

    @setting("plasmac.material.pierce_delay",
             default_value=1.0,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def pierce_delay(self, obj):
        return obj.normalizeValue(self._material.pierce_delay)

    @pierce_delay.setter
    def pierce_delay(self, obj, pierce_delay):
        new_val = obj.normalizeValue(pierce_delay)
        LOG.error("PlasmaC Pierce Delay changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)

    @setting("plasmac.material.cut_height",
             default_value=1.0,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def cut_height(self, obj):
        return obj.normalizeValue(self._material.cut_height)

    @cut_height.setter
    def cut_height(self, obj, cut_height):
        new_val = obj.normalizeValue(cut_height)
        LOG.error("PlasmaC Cut Height changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)

    @setting("plasmac.material.cut_speed",
             default_value=1.0,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def cut_speed(self, obj):
        return obj.normalizeValue(self._material.cut_speed)

    @cut_speed.setter
    def cut_speed(self, obj, cut_speed):
        new_val = obj.normalizeValue(cut_speed)
        LOG.error("PlasmaC Cut Speed changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)

    @setting("plasmac.material.cut_amps",
             default_value=1.0,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def cut_amps(self, obj):
        return obj.normalizeValue(self._material.cut_feed_rate)

    @cut_amps.setter
    def cut_amps(self, obj, cut_amps):
        new_val = obj.normalizeValue(cut_amps)
        LOG.error("PlasmaC Cut Amps changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)

    @setting("plasmac.material.cut_volts",
             default_value=1.0,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def cut_volts(self, obj):
        return obj.normalizeValue(self._material.cut_amps)

    @cut_volts.setter
    def cut_volts(self, obj, cut_volts):
        new_val = obj.normalizeValue(cut_volts)
        LOG.error("PlasmaC Cut Volts changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)

    @setting("plasmac.material.puddle_jump_height",
             default_value=1.0,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def puddle_jump_height(self, obj):
        return obj.normalizeValue(self._material.puddle_jump_height)

    @puddle_jump_height.setter
    def puddle_jump_height(self, obj, puddle_jump_height):
        new_val = obj.normalizeValue(puddle_jump_height)
        LOG.error("PlasmaC Puddle Jump Height changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)

    @setting("plasmac.material.puddle_jump_delay",
             default_value=1.0,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def puddle_jump_delay(self, obj):
        return obj.normalizeValue(self._material.puddle_jump_height)

    @puddle_jump_delay.setter
    def puddle_jump_delay(self, obj, puddle_jump_delay):
        new_val = obj.normalizeValue(puddle_jump_delay)
        LOG.error("PlasmaC Puddle Jump Delay changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)

    @setting("plasmac.material.pause_at_end",
             default_value=1.0,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def pause_at_end(self, obj):
        return obj.normalizeValue(self._material.pause_at_end)

    @pause_at_end.setter
    def pause_at_end(self, obj, pause_at_end):
        new_val = obj.normalizeValue(pause_at_end)
        LOG.error("PlasmaC Puddle Pause at End changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)

    @setting("plasmac.material.gas_pressure",
             default_value=1.0,
             value_type=float,
             min_value=0,
             max_value=5,
             persistent=False)
    def gas_pressure(self, obj):
        return obj.normalizeValue(self._material.pause_at_end)

    @gas_pressure.setter
    def gas_pressure(self, obj, gas_pressure):
        new_val = obj.normalizeValue(gas_pressure)
        LOG.error("PlasmaC Gas Pressure changed: %.4f > %.4f", obj.value, new_val)
        obj.value = new_val
        obj.signal.emit(obj.value)



