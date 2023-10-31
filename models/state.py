#!/usr/bin/python3.
""" State Module for ABNB project """


from models.base_model import BaseModel

class State(BaseModel):
    """State class that inherits from BaseModel."""
    name = ""
    last_name = ""
    age = ""
    birthday = ""
    women = ""
    man = ""
    children = ""
    