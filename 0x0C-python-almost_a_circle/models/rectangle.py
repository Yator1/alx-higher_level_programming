#!/usr/bin/python3

"""
This module contains a class defining a rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    The class inherits from Base
    Attributes:
        __width: width of rectangle
        __height: rectangles height
        __x: rectangles x coordinates
        __y: rectangles y coordinates
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Super class with id"""
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getting the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setting the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0") 
        self.__width = value

    @property
    def height(self):
        """getting the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setting the height"""
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__width = value

    @property
    def x(self):
        """ return the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ set the value of x """
        
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        
        self.__x = value

    @property
    def y(self):
        """ get the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """ set the value of y """
        
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        
        self.__y = value

    def area(self):
        """returns the area value of the rectangle"""
        return (self.__width * self.height)

    def display(self):
        """displayng the Rectangle with '#' characters"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Override __str__ method"""
        new_str = f'[Rectangle] ({self.id}) {self.__x}/{self.__y}'
        new_str += f' - {self.__width}/{self.__height}'
        return (new_str)

    def update(self, *args, **kwargs):
        """ assign an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """Returning dict reps of the rectangle"""
        return ({
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            })
