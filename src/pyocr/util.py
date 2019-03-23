import os

import re


def digits_only(string):
    """Return all digits that the given string starts with."""
    match = re.match(r'\D*(?P<digits>\d+)', string)
    if match:
        return int(match.group('digits'))
    return 0


def is_on_path(exec_name):
    """
    Indicates if the command 'exec_name' appears to be installed.

    Returns:
        True --- if it is installed
        False --- if it isn't
    """
    for dirpath in os.environ["PATH"].split(os.pathsep):
        path = os.path.join(dirpath, exec_name)
        if os.path.exists(path) and os.access(path, os.X_OK):
            return True
    return False
