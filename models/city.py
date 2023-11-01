#!/usr/bin/python3.
"""Define the City class """


from models.base_model import BaseModel
from models.state import State

class City(Basemodel):
    """City Class"""
    state_id = ""
    name = ""
    
    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
