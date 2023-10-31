#!/usr/bin/python3.
""" Review Module for ABNB project """


from models.base_model import BaseModel

class Review(BaseModel):
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
        
        
        return self.text_id