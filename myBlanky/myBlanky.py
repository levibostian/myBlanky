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
from docopt import docopt
from myBlanky import _version


def main(arguments):

    if arguments['blanky']:
        blanky = arguments['blanky']
        if is_blanky_available(blanky):
            copy_blanky_to_destination(blanky)
        else:
            print("Given blanky: %s name not available. Choose from following:")
            print_blankys_list()

    elif arguments['list']:
        print_blankys_list()

    else:
        print(__doc__)


if __name__ == '__main__':
    cmd_args = docopt(__doc__, version=_version)

    main(cmd_args)