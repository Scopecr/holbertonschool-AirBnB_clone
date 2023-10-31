#!/usr/bin/python3.
"""Define the City class """


from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel."""
    state_id: str = ""
    name: str = ""
    
def state_id(self):
    """Returns the state id."""
    return self.state_id

def name(self):
    """Returns the name."""
    return self.name

# Compare this snippet from models/amenity.py:

if __name__ == '__main__':
    HBNBCommand().cmdloop()

