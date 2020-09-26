import os, sys
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("entry_points.ini", "r") as fh:
    entry_points = fh.read()


# list of (destination, source_file) tuples
DATA_FILES = [
    # ('~/', ['scripts/.xsessionrc',]),
]

# list of (destination, source_dir) tuples
DATA_DIRS = [
    ('share/plasma_flat/linuxcnc/configs/sim.plasma-flat/', 'linuxcnc/configs/sim.plasma-flat'),
    ('share/plasma_flat/linuxcnc/nc_files/plasma-flat', 'linuxcnc/nc_files/plasma-flat'),
]


def data_files_from_dirs(data_dirs):
    data_files = []
    for dest_dir, source_dir in data_dirs:
        dest_dir = os.path.expandvars(dest_dir)
        for root, dirs, files in os.walk(source_dir):
            root_files = [os.path.join(root, i) for i in files]
            dest = os.path.join(dest_dir, os.path.relpath(root, source_dir))
            data_files.append((dest, root_files))

    return data_files


data_files = [(os.path.expanduser(dest), src_list) for dest, src_list in DATA_FILES]
data_files.extend(data_files_from_dirs(DATA_DIRS))


setup(
    name="plasma-flat",
    version="0.0.1",
    author="Kurt Jacobson",
    author_email="<doe.john@example.com>",
    description="Plasma Flat - A QtPyVCP based Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kurtjacobson/plasma-flat",
    download_url="https://github.com/kurtjacobson/plsama-flat/tarball/master",
    packages=find_packages(),
    data_files=data_files,
    include_package_data=True,
    entry_points=entry_points,
    # install_requires=[
    #    'qtpyvcp',
    # ],
)
