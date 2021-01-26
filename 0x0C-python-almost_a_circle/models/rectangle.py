#!/usr/bin/python3
'''Rectangle module'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Class Constructor'''

        self.int_validator("width", width)
        self.__width = width
        self.int_validator("height", height)
        self.__height = height
        super().__init__(id)
        self.int_validator("x", x)
        self.__x = x
        self.int_validator("y", y)
        self.__y = y

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @property
    def height(self):
        """Height Getter"""
        return self.__height

    @property
    def x(self):
        """x Getter"""
        return self.__x

    @property
    def y(self):
        """y Getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """Width Setter
        """
        self.int_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Height Setter
        """
        self.int_validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """x Setter
        """
        self.int_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """y Setter
        """
        self.int_validator("y", value)
        self.__y = value

    def area(self):
        '''Returns area of rectangle'''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print("", end=" ")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''Str method'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        '''Updates the values of Rectangle'''
        argumentos = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for i in range(len(args)):
                self.int_validator(argumentos[i], args[i])
                setattr(self, argumentos[i], args[i])
        else:
            for key, value in kwargs.items():
                self.int_validator(key, value)
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "width": self.__width, "height": self.__height}
