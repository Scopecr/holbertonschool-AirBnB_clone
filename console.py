#!/usr/bin/python3.
""" This module instantiates an object of class FileStorage """


import models
from models.engine.file_storage import FileStorage
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command Line Interpreter for ABNB project"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ 
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """ 
        Handle the EOF (End of File) signal.
        """
        print()
        return True

    def emptyline(self):
        """
        Override the default behavior when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        new_instance = models.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance based on class name and id.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id.
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            models.storage.save()

    def do_all(self, arg):
        """
        Print string representations of all instances based on class name (optional).
        Usage: all or all <class_name>
        """
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            if args[0] not in models.classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in objects.values() if obj.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """
        Update an instance based on class name and id by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            attribute_name = args[2]
            attribute_value = args[3]
            setattr(objects[key], attribute_name, attribute_value)
            models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
