#!/usr/bin/python3
"""
Console module for command line interpreter
"""

import cmd
import shlex
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for command line interpreter
    """
    prompt = '(hbnb) '
    file_path = "file.json"
    classes = {
        "BaseModel": BaseModel,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file,
        and prints the id of the new instance
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in FileStorage._FileStorage__objects:
                print(FileStorage._FileStorage__objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in FileStorage._FileStorage__objects:
                del FileStorage._FileStorage__objects[key]
                FileStorage().save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances or all instances
        of a specified class
        """
        args = shlex.split(arg)
        if not args:
            print([str(value) for value in FileStorage._FileStorage__objects.values()])
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_objects = [str(value) for key, value in FileStorage._FileStorage__objects.items() if args[0] in key]
            print(class_objects)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating
        attribute
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in FileStorage._FileStorage__objects:
                setattr(FileStorage._FileStorage__objects[key], args[2], args[3])
                FileStorage().save()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """
        Quits the command interpreter
        """
        return True

    def do_EOF(self, arg):
        """
        Quits the command interpreter when EOF is reached
        """
        return True

    def emptyline(self):
        """
        Does nothing when an empty line is entered
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
