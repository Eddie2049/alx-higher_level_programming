#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Repr. a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict. repr. of the Student."""
        return self.__dict__
