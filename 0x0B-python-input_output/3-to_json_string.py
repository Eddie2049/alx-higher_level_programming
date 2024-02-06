#!/usr/bin/python3
"""string-to-JSON."""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of a string object."""
    return json.dumps(my_obj)
