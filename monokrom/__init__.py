#!/usr/bin/env python

"""Main entry point for MyVCP.

This module contains the code necessary to be able to launch QControl
directly from the command line, without using qtpyvcp. It handles
parsing command line args and starting the main application.

Example:
    Assuming the dir this file is located in is on the PATH, you can
    launch MyVCP by saying::

        $ myvcp --ini=/path/to/config.ini [options ...]

    Run with the --help option to print a full list of options.

"""


cmd_doc = """
{vcp_name} - A QtPyVCP based Virtual Control Panel for LinuxCNC.

Usage:
  {vcp_cmd} --ini INI [options]
  {vcp_cmd} --install-sim
  {vcp_cmd} (-h | --help)
  {vcp_cmd} (-v | --version)
  {vcp_cmd} (-i | --info)

Required Arguments:
  --ini INI            Path to INI file, relative to ~/linuxcnc/configs.

Commands:
  --install-sim        Installs LinuxCNC configs, data files etc. in the correct
                       locations. This should always be run after updating.

Display  Options:
  --theme THEME        The Qt theme to use, defaults to system theme.
  --stylesheet STYLESHEET
                       Path to QSS file containing styles to be applied
                       to specific Qt and/or QtPyVCP widget classes.
  --size WIDTHxHEIGHT  Initial size of the window in pixels.
  --position XPOSxYPOS
                       Initial position of the window, specified as the
                       coordinates of the top left corner of the window
                       relative to the top left corner of the screen.
  --fullscreen BOOL    Flag to start with window fullscreen.
  --maximize BOOL      Flag to start with window maximized.
  --hide-menu-bar      Hides the menu bar, if present.
  --hide-status-bar    Hides the status bar, if present.
  --hide-cursor        Hide the mouse cursor.
  --confirm-exit BOOL  Whether to show dialog to confirm exit.

Application Options:
  --log-level=(DEBUG | INFO | WARN | ERROR | CRITICAL)
                       Sets the log level. Default INFO.
  --config-file PATH   Specify the YML config file relative to $CONFIG_DIR.
  --log-file PATH      Specify the log file relative to $CONFIG_DIR.
  --qt-api (pyqt5 | pyqt | pyside2 | pyside)
                       Specify the Qt Python binding to use.
  --perfmon            Monitor and log system performance.
  --develop            Development mode. Enables live reloading of QSS styles.
  --command_line_args <args>...
                       Additional args passed to the QtApplication.

General Options:
  -h --help            Show this help and exit.
  -v --version         Show version and exit.
  -i --info            Show system info and exit.

Note:
  When specifying {vcp_name} in the INI using [DISPLAY]DISPLAY={vcp_cmd} [...]
  the --ini parameter will be passed by the linuxcnc startup script so does
  not need to be specified.

"""

__version__ = '0.0.1'

import os
import qtpyvcp
from distutils.dir_util import copy_tree

VCP_DIR = os.path.realpath(os.path.dirname(__file__))


def main(machine_type='plasma', opts=None):

    if opts is None:
        from qtpyvcp.utilities.opt_parser import parse_opts
        opts = parse_opts(doc=cmd_doc,
                          vcp_cmd='monokrome-{}'.format(machine_type),
                          vcp_name='Monokrome {}'.format(machine_type.capitalize()),
                          vcp_version=__version__)

        if opts.install_sim:
            src = os.path.join(VCP_DIR, '../linuxcnc')
            if not os.path.isdir(src):
                src = os.path.expanduser('~/.local/share/monokrom/linuxcnc')

            copy_tree(src, os.path.expanduser('~/linuxcnc'), update=1)
            print("Successfully copied sim configs to ~/linuxcnc.")
            return

    # choose the right config file for the machine type
    config_file = os.path.join(VCP_DIR, machine_type, 'config.yml')

    qtpyvcp.run_vcp(opts, config_file)


if __name__ == '__main__':
    main()
