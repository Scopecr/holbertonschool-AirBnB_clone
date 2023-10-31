#!/usr/bin/python3.
""" City Module for HBNB project """


from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel."""
    state_id: str = ""
    name: str = ""
    
    def state_id(self):
        """Returns the state id"""
        if self.state_id:

        
        return self.state_id
    
if __name__ == '__main__':
    HBNBCommand().cmdloop() 
