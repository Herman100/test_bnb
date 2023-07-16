#!/usr/bin/python3
"""This module represents a class Review that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """this is the review class of base model"""

    place_id = ""
    user_id = ""
    text = ""
