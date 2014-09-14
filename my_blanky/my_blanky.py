"""myBlanky. Get building faster!

Usage:
  myblanky (--blanky=<blanky-name>) [--dir=<path>]
  myblanky list
  myblanky (-h | --help)
  myblanky (-v | --version)

Options:
  -h --help          Show this screen.
  -v --version       Show myBlanky version.
  --blanky=<name>    Name of blank project to copy.
  --dir=<path>       Output dir. If not given, current directory used.
  list               List all available blank projects to choose from.
"""

import sys
import os
import shutil
from docopt import docopt
from my_blanky import file_system_util
from my_blanky import version


def get_available_blanky_names():
    parent_dir_directories = []
    for item in os.listdir(file_system_util.get_blanky_projects_dir_path()):
        if not os.path.isfile(item):
            parent_dir_directories.append(item)

    return parent_dir_directories


def is_blanky_available(blank_name):
    return blank_name in get_available_blanky_names()


def copy_blanky_to_destination(blanky_name, dest_path):
    try:
        shutil.copytree(os.path.join(file_system_util.get_parent_dir_path(), blanky_name), dest_path)
    except shutil.Error as e:
        return e


def get_printable_blankys_list():
    blank_list = ""
    for blanky in get_available_blanky_names():
        blank_list += blanky + "\n"
    return blank_list[:-1]


def get_absolute_path_from_relative(dir_name):
    return os.path.join(file_system_util.get_current_dir_path(), dir_name)


def main():
    cmd_args = docopt(__doc__, version=version.get_version())
    my_blanky(cmd_args)
    # print("current dir path: " + get_current_dir_path())
    # print("current dir name: " + get_current_dir_name())
    # print("parent dir path: " + get_parent_dir_path())
    # print("parent dir name: " + get_parent_dir_name())
    # print("current dir: " + os.getcwd())
    # print()
    # print("current dir list:")
    # print(os.listdir(os.getcwd()))
    # print("blankys dir path: " + get_blanky_projects_dir_path())
    # print()
    # print("blankys here:")
    # print(os.listdir(get_blanky_projects_dir_path()))
    # print()
    # print("curr dir files:")
    # print(os.listdir(get_current_dir_path()))
    # print()
    # print("parent dir files:")
    # print(os.listdir(get_parent_dir_path()))


def my_blanky(arguments):

    if 'blanky' in arguments:
        blanky = arguments['blanky']
        if is_blanky_available(blanky):
            destination_dir = arguments['dir']
            if not destination_dir.startswith(os.sep):
                destination_dir = get_absolute_path_from_relative(destination_dir)

            dir_to_copy_to = ""
            if arguments['dir'] and os.path.isdir(arguments['dir']):
                dir_to_copy_to = arguments['dir']
            else:
                dir_to_copy_to = file_system_util.get_current_dir_path()
            try:
                copy_blanky_to_destination(blanky, dir_to_copy_to)
            except shutil.Error as e:
                print("You cannot copy the same directory.")
                sys.exit(1)
            except OSError as e:
                print("Directory does not exist.")
                sys.exit(1)
        else:
            print("Given blanky: %s name not available. Choose from following:")
            get_printable_blankys_list()

    elif 'list' in arguments:
        get_printable_blankys_list()

    else:
        print(__doc__)


if __name__ == '__main__':
    main()