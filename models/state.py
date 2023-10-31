#!/usr/bin/python3.
""" State Module for ABNB project """


from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from cmd import Cmd
import json

class State(BaseModel):
    """State class that inherits from BaseModel."""
    first_name = ""
    last_name = ""
    age = ""
    birthday = ""
    women = ""
    man = ""
    children = ""


class State(BaseModel):
    """State class that inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a new State."""
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
      