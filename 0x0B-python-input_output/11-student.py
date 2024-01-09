#!/usr/bin/python3

"""
This file contains one class Student
it defines a student which has two public method that retrieves
a dictionary representation of a student instance
and replaces all attributes of a student instance
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        initializes a student object with first_name, last_name and age
        attributes

        Args:
            first_name (str): the Students first name
            last_name (str): the students last name
            age (int): the age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a student instance

        Args:
            attrs (list, optional): list of attribute names to be retrieved
                if None, all attributes are retrieved

        Return:
            dict: a dictionary containing the attributes of the student
        """
        if attrs is None:
            attrs = vars(self).keys()
        json_dict = {}
        for att in attrs:
            if hasattr(self, att):
                json_dict[att] = getattr(self, att)

        return (json_dict)

    def reload_from_json(self, json):
        """
        Replaces all attributes of the student intanince
        with values from the dictionary

        Args:
            json (dict): dictionary containing attribute names and their values
        """
        for att, value in json.items():
            setattr(self, att, value)
