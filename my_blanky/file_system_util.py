"""
File system util class for receiving various file system information.

WARNING: Place file_system_util.py in same directory of file calling the functions.
         Functions have not been tested to be called from some random location.
"""

import os

BLANKY_PROJS_DIR_NAME = "blankys"


def get_current_dir_name():
    return get_current_dir_path().split(os.sep)[-1]


def get_current_dir_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_parent_dir_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def get_parent_dir_name():
    return get_parent_dir_path().split(os.sep)[-1]


def get_blanky_projects_dir_path():
    return os.path.join(get_parent_dir_path(), BLANKY_PROJS_DIR_NAME)