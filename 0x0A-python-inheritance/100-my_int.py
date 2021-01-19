#!/usr/bin/python3
'''My int module'''


class MyInt(int):
    '''My int class'''

    def __init__(self, value):
        '''Constructor'''
        self.__value = value

    def __eq__(self, value):
        """compare object if is equal than"""
        return self.__value != self.__value

    def __ne__(self, value):
        """compare object if is not equal than"""
        return self.__value == self.__value
