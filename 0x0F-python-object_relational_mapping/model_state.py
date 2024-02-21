#!/usr/bin/python3
"""
Module containing the class definition of a State
and an instance Base = declarative_base():
"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    State - contains the class definition of a State

    Args:
        Base (SuperClass): declarative base of sqlalchemy
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
