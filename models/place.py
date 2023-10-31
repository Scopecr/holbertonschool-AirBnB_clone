#!/usr/bin/python3.
""" Place Module for HBNB project """

from datetime import datetime
from console import HBNBCommand
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
    
    def city_id(self):
        """Returns the city id."""
        return self.city_id
    
    def user_id(self):
        """Returns the user id."""
        return self.user_id
    def name(self):
        """Returns the name."""
        return self.name
    def description(self):
        """Returns the description."""
        return self.description
      
    def number_rooms(self):
        """Returns the number of rooms."""
        return self.number_rooms
    
    def number_bathrooms(self):
        """Returns the number of bathrooms."""
        return self.number_bathrooms
    
    def max_guest(self):
        """Returns the max guest."""
        return self.max_guest
      
    def price_by_night(self):
        """Returns the price by night."""
        return self.price_by_night
    def latitude(self):
        """Returns the latitude."""
        return self.latitude
    
    def longitude(self):
        """Returns the longitude."""
        return self.longitude
    
    def amenity_ids(self):
        """Returns the amenity ids."""
        return self.amenity_ids
         
    
    def __init__(self, *args, **kwargs):
        """Instantiates a new Place."""
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
    
    # Compare this snippet from models/city.py:
    
  if __name__ == '__main__':
    HBNBCommand().cmdloop()  
