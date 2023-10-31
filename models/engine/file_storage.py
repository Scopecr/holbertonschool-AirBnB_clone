#!/user/bin/python3
""" File Storage Module for ABNB project """


import json

class FileStorage:
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store all objects by <class name>.id

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the object in __objects with the key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            file.write(json.dumps(obj_dict))

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists.
        """
        import models
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.loads(file.read())
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    self.__objects[key] = models.classes[cls_name](**value)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()