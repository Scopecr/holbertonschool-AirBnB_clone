#!/usr/bin/python3.
""" Place Module for HBNB project """

from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from cmd import Cmd
import json

class Place(BaseModel):
    """Place class that inherits from BaseModel."""
    
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: str = 0
    number_bathrooms: str = 0
    max_guest: str = 0
    price_by_night: str = 0
    latitude: str = 0.0
    longitude: str = 0.0
    amenity_ids: str = []
    
  if __name__ == '__main__':
    HBNBCommand().cmdloop()  
