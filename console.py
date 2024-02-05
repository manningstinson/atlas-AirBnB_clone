#!/usr/bin/python3
"""
Console module for AirBnB project
"""

import cmd
from models.base_model import BaseModel
from models.user import User  # Import User class
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class inherits from cmd.Cmd
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line should not execute anything"""
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel or User.

        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show string representation of an instance.

        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            cls = eval(arg_list[0])
        except Exception as e:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = "{}.{}".format(arg_list[0], instance_id)
        all_instances = storage.all()
        if key in all_instances:
            print(all_instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy an instance based on class name and id.

        Usage: destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            cls = eval(arg_list[0])
        except Exception as e:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = "{}.{}".format(arg_list[0], instance_id)
        all_instances = storage.all()
        if key in all_instances:
            del all_instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print string representation of all instances.

        Usage: all <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)
        except Exception as e:
            print("** class doesn't exist **")
            return

        all_instances = storage.all()
        result = [str(value) for key, value in all_instances.items()
                  if key.startswith(arg + ".")]
        print(result)

    def do_update(self, arg):
        """
        Update an instance based on class name and id.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            cls = eval(arg_list[0])
        except Exception as e:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = "{}.{}".format(arg_list[0], instance_id)
        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        attribute_name = arg_list[3]
        attribute_value = arg_list[4]
        instance = all_instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def precmd(self, line):
        """
        Override the precommand method to handle empty lines with spaces
        """
        if not line.strip():
            return ""
        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
