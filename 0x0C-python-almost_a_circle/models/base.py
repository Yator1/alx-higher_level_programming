#!/usr/bin/python3

"""
This module contains one class Base
"""
import json
import csv


class Base:
    """
    This class Base has one private attribute
    Attrubutes:
        __nb_objects: initialized to 0. counts objects with no Id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method initialises id.
        Increment __nb_objects if id is None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string represantion of list_objs"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
            )
        with open(filename, 'w') as file:
            file.write(json_string)
    
    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string"""
        if json_string is None or json_string == '':
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns the list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                obj_dicts = cls.from_json_string(json_string)
                return ([cls.create(**obj_dict) for obj_dict in obj_dicts])
        except FileNotFoundError:
            return ([])

    """csv files"""
    @classmethod
    def save_to_file_csv(cls, list_obj):
        """serialize objects to CSV file"""
        if list_obj is None:
            list_obj = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_obj:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                obj_list = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(
                            int(row[0]), int(row[1]), int(row[2]),
                            int(row[3]), int(row[4]))
                    elif cls.__name__ == "Square":
                        obj = cls(
                            int(row[0]), int(row[1]), int(row[2]),
                            int(row[3]))
                    obj_list.append(obj)
                return (obj_list)
        except FileNotFoundError:
            return ([])
