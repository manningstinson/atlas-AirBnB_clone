#!/usr/bin/python3
"""
Console 0.0.1
mandatory
Score: 0.00% (Checks completed: 0.00%)
"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
