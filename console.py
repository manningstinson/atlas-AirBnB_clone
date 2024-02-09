#!/usr/bin/python3
"""Module for console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)."""
        print()
        return True

    def do_help(self, arg):
        """Help command to display available commands."""
        cmd.Cmd.do_help(self, arg)

    def do_emptyline(self):
        """Do nothing on empty input."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
