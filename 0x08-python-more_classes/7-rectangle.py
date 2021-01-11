#!/usr/bin/python3
"""Module about Rectangle Class"""


class Rectangle:
    """Rectangle Class"""
    number_of_instances = 0
    print_symbol = "#"    

    def __init__(self, width=0, height=0):
        """Init constructor"""
        if type(width) != int: 
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width= width
        type(self).number_of_instances += 1

        
    def __str__(self):
        '''Print the rectangle with the character #'''
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec += str(self.print_symbol)
            if i < self.__height - 1:
                rec += '\n'
        return rec

    def __repr__(self):
        '''Print the rectangle with the character #'''
        return "Rectangle({}, {})".format(self.__width, self.__height)      
    
    @property
    def width(self):
        """Width Getter
        """
        return self.__width
    
    @property
    def height(self):
        """Height Getter
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Width Setter
        """
        if type(value) != int: 
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Height Setter
        """
        if type(value) != int: 
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Calculates area of rectangle'''
        return self.__width * self.__height
    
    def perimeter(self):
        '''Calculates perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __del__(self):
        '''deletes instance'''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1