#!/usr/bin/python3
'''Base module'''
import json
import csv


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Class constructor'''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''json dumps'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    '''@classmethod
    def save_to_file(cls, list_objs):
        writes the JSON string representation of list_objs to a file
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w") as f:
            if list_objs is None:
                f.write = "[]"
            else:
                for obj in list_objs:
                    f.write(Base.to_json_string(obj.to_dictionary()))'''

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        classmethod save_to_file
        '''
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as file:
            jStr = []
            if list_objs is not None:
                for obj in list_objs:
                    jStr.append(cls.to_dictionary(obj))
                jStr = Base.to_json_string(jStr)
                file.write(str(jStr))
            else:
                file.write(str(jStr))

    @staticmethod
    def from_json_string(json_string):
        '''json loads'''
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    '''@classmethod
    def create(cls, **dictionary):
        returns an instance with all attributes already set
        dummy = cls(2, 2, 0, 0, 1)
        dummy.update(**dictionary)
        return dummy'''

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes already set
        '''
        if cls.__name__ is 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ is 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    def int_validator(self, name, value):
        '''Integer Validator for width and lenght'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and (name == "width" or name == "height"):
            raise ValueError("{} must be > 0".format(name))
        elif value < 0 and (name == "x" or name == "y"):
            raise ValueError("{} must be >= 0".format(name))

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        lists = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                for obj in cls.from_json_string(f.read()):
                    lists.append(cls.create(**obj))
                return lists
        except Exception:
            return lists

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        classmethod save_to_file
        '''
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as f:
            csv_write = csv.writer(f, delimiter=',')
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_write.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_write.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        '''
        classmethod load_to_file
        '''
        lists = []
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f, delimiter=',')
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]), "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(
                            args[1]), "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    lists.append(obj)
                return lists
        except Exception:
            return lists
