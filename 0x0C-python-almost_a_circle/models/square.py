#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter and Setter for size"""
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        s = f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
        return (s)
