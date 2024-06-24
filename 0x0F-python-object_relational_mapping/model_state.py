#!/usr/bin/python3
"""
Python file that contains the class definition
of a State and an instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":

    Base = declarative_base()

    class State(Base):
        """State class definition
        Attributes:
                __tablename__ (str): The name of the table in the database
                id (int): The id of the state
                  (auto-generated, unique, primary key)
                name (str): The name of the state
        """
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
