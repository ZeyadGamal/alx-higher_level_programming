#!/usr/bin/python3
"""Defines a Rectangle class """


class Rectangle:
    """Represent a rectangle
        Attributes:
            number_of_instances (int): number of rectangles
            print_symbol (string): symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """retrieve width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """prints rectangle with print symbol"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for i in range(self.__height):
            [r.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """return string representation of rectangle"""
        rectangle = "Rectangle(" + str(self.__width) + ", "
        rectangle += str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """prints a message after deleting a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return bigger rectangle

        Args:
            rect_1 (Rectangle): rectangle 1
            rect_2 (Rectangle): rectangle 2
        Raises:
            TypeError: if either is not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """returns a new rectangle instance with width == height == size

        Args:
            size (int): size of new rectangle
        """
        return (cls(size, size))
