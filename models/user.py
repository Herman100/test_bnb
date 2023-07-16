#!/usr/bin/python3
"""This module represents a class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """this is the User class of base model"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
