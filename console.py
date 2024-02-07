import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class implementing a command interpreter."""

    prompt = '(hbnb) '
    __classes = {"BaseModel": BaseModel, "User": User}  # Add User class

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Exit the program when EOF is reached."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.__classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = FileStorage().all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = FileStorage().all()
            if key in all_objs:
                del all_objs[key]
                FileStorage().save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        args = arg.split()
        all_objs = FileStorage().all()
        if len(args) == 0:
            print([str(obj) for obj in all_objs.values()])
        elif args[0] in HBNBCommand.__classes:
            print([str(obj) for key, obj in all_objs.items() if key.startswith(args[0])])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = FileStorage().all()
            if key in all_objs:
                setattr(all_objs[key], args[2], args[3])
                all_objs[key].save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
