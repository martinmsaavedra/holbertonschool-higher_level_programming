#!/usr/bin/python3
'''Rectangle module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """new class"""

    def __init__(self, size, x=0, y=0, id=None):
        '''Square constructor'''
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """y Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Width Setter
        """
        self.int_validator("width", value)
        self.__size = value

    def __str__(self):
        '''Str method'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self._Rectangle__x,
                                                 self._Rectangle__y,
                                                 self.__size)

    def update(self, *args, **kwargs):
        """args and kwargs"""
        argumentos = ["id", "size", "x", "y"]
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
        return {"x": self._Rectangle__x, "y": self._Rectangle__y,
                "id": self.id, "size": self.__size}
