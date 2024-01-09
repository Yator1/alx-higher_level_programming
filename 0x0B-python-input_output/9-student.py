#!/usr/bin/python3

"""
This file contains one class Student
it defines a student which has one public method that retrieves
a dictionary representation of a student instance
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a student instance

        Return:
            dict: a dictionary containing the attributes of the student
        """
        json_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }

        return (json_dict)
