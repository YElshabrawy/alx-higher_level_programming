#!/usr/bin/python3
'''module'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''State Table'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
