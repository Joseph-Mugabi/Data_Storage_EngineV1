#!/usr/bin/python3
""" Class Data"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Text, text


class Data(BaseModel, Base):
    """ representation of a data"""
    __tablename__ = 'datas'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128),  nullable=False)
    value = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """initialising the data"""
        super().__init__(*args, **kwargs)
