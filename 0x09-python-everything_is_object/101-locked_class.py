#!/usr/bin/python3
"""Defines locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    except attributes called 'first_name'.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        pass
