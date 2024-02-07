#!/usr/bin/python3
"""
Console 0.0.1
mandatory
Score: 0.00% (Checks completed: 0.00%)
"""

import cmd
import json
import datetime
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class implementing a command interpreter.
    """
    prompt = '(hbnb) '
    classes = ["BaseModel"]

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
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        all_objs = BaseModel.all()
        for obj in all_objs:
            if obj.id == args[1]:
                print(obj)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        all_objs = BaseModel.all()
        for obj in all_objs:
            if obj.id == args[1]:
                del obj
                BaseModel.save_to_file()
                return
        print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        all_objs = []
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return
            all_objs = BaseModel.all(arg)
        else:
            all_objs = BaseModel.all()

        print([str(obj) for obj in all_objs])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        all_objs = BaseModel.all()
        for obj in all_objs:
            if obj.id == args[1]:
                if len(args) < 4:
                    print("** attribute name missing **")
                    return

                if len(args) < 5:
                    print("** value missing **")
                    return

                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()
                return
        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
