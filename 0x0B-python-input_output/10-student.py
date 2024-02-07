#!/usr/bin/python3
"""defining a class Student."""


class Student:
    """Repr. a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict. repr. of the Student.
        """
        if (type(attrs) is list and
                all(type(elem) is str for elem in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
