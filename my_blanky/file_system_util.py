"""
File system util class for receiving various file system information.

WARNING: Place file_system_util.py in same directory of file calling the functions.
         Functions have not been tested to be called from some random location.
"""

import os


def get_current_dir_name():
    return get_current_dir_path().split('/')[-1]


def get_current_dir_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_parent_dir_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def get_parent_dir_name():
    return get_parent_dir_path().split('/')[-1]