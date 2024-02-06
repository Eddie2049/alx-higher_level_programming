#!/usr/bin/python3
"""a JSON-to-python_object function."""
import json


def from_json_string(my_str):
    """function that returns the Python object
    representation of a JSON string.
    """
    return json.loads(my_str)
