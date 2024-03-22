#!/usr/bin/python3

"""
a python file that contains the class definition of a State
and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class State that inherits Base
    links to the MySQL table states
    class attribute:
        id-represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
        name- represents a column of a string with max 128
        characters and can’t be null
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
