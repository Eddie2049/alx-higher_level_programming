#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Prints an integer with "{:d}".format().
    Args: value
    Return: True/ False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
