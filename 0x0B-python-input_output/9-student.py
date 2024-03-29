#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation of student"""
        return (self.__dict__)
