#!/usr/bin/python3
"""
Console module implementing a command interpreter for the AirBnB clone project.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class implementing a command interpreter.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program when EOF is reached
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a specified class
        Usage: create <class_name>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ("BaseModel", "User"):  # Add more classes as needed
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        """
        Print all string representation of all instances
        Usage: all [optional_class_name]
        """
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        try:
            class_name = eval(arg).__name__
        except NameError:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objects.items() if key.startswith(class_name)])

    def do_update(self, arg):
        """
        Update an instance based on the class name and id
        Usage: update
        <class_name> <id> 
        <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        attr_name = args[2]
        attr_value = args[3]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        obj = objects[key]
        setattr(obj, attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
