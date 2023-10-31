#!/usr/bin/python3.
""" User Module for HBNB project """


from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from cmd import Cmd
import json

class User(BaseModel):
    """User class that inherits from BaseModel."""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name:str = ""
    
    def __init__(self, *args, **kwargs):
        """Instantiates a new User."""
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
