#!usr/bin/python3
""" HBNBCommand Module for ABNB project """

import models
from models.base_model import BaseModel

# BEGIN: HBNBCommand class
from datetime import datetime
import uuid
import models

class BaseModel:
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String representation """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Save method """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Dictionary representation """
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

# END: BaseModel class

from console import HBNBCommand

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    