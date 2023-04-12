#!/usr/bin/python3
""" Class Settings"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Text, text
from sqlalchemy.orm import relationship

class Settings(BaseModel, Base):
    """representation of user settings"""
    __tablename__ = 'settings' 
    user_id = Column(String(128), ForeignKey('users.id'), nullable=False, unique=True)
    theme = Column(String(60), nullable=True)
    language = Column(String(60), nullable=True)
    notifications = Column(Integer, nullable=True)
    #user = relationship('User', backref='settings')

    def __init__(self, *args, **kwargs):
        """initialising the user settings"""
        super().__init__(*args, **kwargs)
