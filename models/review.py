#!/usr/bin/python3.
""" Review Module for ABNB project """


from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    
    place_id: str = ""
    user_id: str = ""
    text_id: str = ""

def __init__(self, *args, **kwargs):
    class Review(BaseModel):
        """Review class that inherits from BaseModel."""

        place_id: str = ""
        user_id: str = ""
        text_id: str = ""

        def __init__(self, *args, **kwargs):
            """Instantiates a new Review."""
            super().__init__(*args, **kwargs)

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

        def __init__(self, *args, **kwargs):
            """Instantiates a new Review."""
            super().__init__(*args, **kwargs)

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