#!/usr/bin/python3.
""" User Module for HBNB project """


from console import HBNBCommand
from models.base_model import BaseModel
from datetime import datetime
import uuid
import models
from models import storage


class User(BaseModel):
    """User class that inherits from BaseModel."""
    
    email: str = "" # it will be the User.id
    password: str = "" # it will be the User.id
    first_name: str = ""# it will be the User.id
    last_name:str = "" # it will be the User.id
    
    @property
    def email(self):
        """Returns the email."""
        
        if self.email is not None: # if email is not empty
            return self.email
    
    @property
    def password(self):
        """Returns the password."""
        
        if self.password is not None:
            return self.password
    
    @property
    def first_name(self):
        """Returns the first name."""
        return self.first_name
    
    @property
    def last_name(self):
        """Returns the last name."""
        return self.last_name
    
    def __init__(self, *args, **kwargs):
        """Instantiates a new User."""

        super().__init__(*args, **kwargs)
        if kwargs: # if kwargs is not empty
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)

# Compare this snippet from models/user.py:

if __name__ == '__main__':
    HBNBCommand().cmdloop()
