#!/usr/bin/python3
"""This module defines a class HBNBCommand"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

from models import storage


class HBNBCommand(cmd.Cmd):
    """Class that contains the entry point of the command interpreter."""

    prompt = '(hbnb)'

    def do_help(self, arg):
        """Help command to show the documentation of the commands."""
        cmd.Cmd.do_help(self, arg)

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in globals():
            print("** class doesn't exist **")
            return
        else:
            """creates new instance for the class"""
            new_instance = globals()[arg]()
            """saves the new instance"""
            new_instance.save()
            """print id of instance"""
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id."""
        args = arg.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in globals() or not \
                issubclass(globals()[args[0]], BaseModel):
            print("** class doesn't exist **")
            return
        # & Check if the id is provided
        if len(args) == 1:
            print("** instance id missing **")
            return
        # & Create a key with the class name and id
        key = args[0] + "." + args[1]
        # & Check if the instance exists
        if key in storage.all():
            # & Print the instance
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file)."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name."""
        if arg not in ["BaseModel", "User", "Place", "State", "City",
                       "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if arg:
                    if arg in key:
                        print(value)
                else:
                    print(value)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
