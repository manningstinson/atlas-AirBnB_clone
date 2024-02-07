#!/usr/bin/python3
"""
Console module for AirBnB project.

This module provides a command-line
interface for interacting with the AirBnB project.
"""

import cmd
from models.base_model import BaseModel
from models.user import User  # Import User class
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class inherits from cmd.Cmd.
    This class represents the
    command-line interface for the AirBnB project.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Empty line should not execute anything."""
        pass

    def do_create(self, arg):
        """
        Create a new instance of
        BaseModel, User, or any other class.

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
            print("** {}".format(e))

    # Other methods...

    def precmd(self, line):
        """
        Override the precommand
        method to handle empty lines with spaces.
        """
        if not line.strip():
            return ""
        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
