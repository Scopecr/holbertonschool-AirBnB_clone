#!/usr/bin/python3.
""" Review Module for ABNB project """


from datetime import datetime
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from cmd import Cmd
import json

class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    
    place_id: str = "" # it will be the Place.id
    user_id: str = "" # it will be the User.id
    text_id: str = "" # it will be the review text

        def place_id(self):
            """Returns the place id."""
            return self.place_id

        def user_id(self):
            """Returns the user id."""
            return self.user_id

        def text_id(self):
            """Returns the text id."""
            if self.text is not None:
                return self.text
            return self.text_id
        """Review class that inherits from BaseModel."""

        place_id: str = ""
        user_id: str = ""
        text_id: str = ""


        def place_id(self):
            """Returns the place id."""
            return self.place_id

        def user_id(self):
            """Returns the user id."""
            return self.user_id

        def text_id(self):
            """Returns the text id."""
      
            if self.text is not None:
                return self.text
            return self.text_id


 # Compare this snippet from models/review.py:
        
    if __name__ == '__main__':
        HBNBCommand().cmdloop()
    