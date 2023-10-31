#!/usr/bin/python3
<<<<<<< HEAD
""" Amenity Module for HBNB project"""


=======
"""Defines the Amenity class"""
>>>>>>> 97d5f613968d639c913ef1a9ce20ef2bce6509b3
from models.base_model import BaseModel
from datetime import datetime
from console import HBNBCommand


<<<<<<< HEAD
class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name: str = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a new Amenity."""
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
  
=======

class Amenity(BaseModel):
    """Represent an Amenity object"""
    name = ""
>>>>>>> 97d5f613968d639c913ef1a9ce20ef2bce6509b3
