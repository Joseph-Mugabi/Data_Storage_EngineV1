#!/usr/bin/python3
"""
Class User
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """the representation of a class  User"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        location = Column(String(128), nullable=True)
        contact = Column(String(20), nullable=True)
        data = relationship('Data', backref='user', cascade='all, delete')
        settings = relationship('Settings', uselist=False, backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        location = ""
        contact = ""

    def __init__(self, *args, **kwargs):
        """ Initialisation of the User"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
