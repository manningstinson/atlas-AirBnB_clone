#!/usr/bin/python3
"""Command interpreter module"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
  """Command interpreter class"""
  prompt = "(hbnb) "

  def do_quit(self, arg):
    """Quit command to exit the program"""
    return True

  def do_EOF(self, arg):
    """EOF command to exit the program"""
    print()
    return True

  def emptyline(self):
    """Called when an empty line is entered"""
    pass

  def do_create(self, arg):
    """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
    if not arg:
      print("** class name missing **")
      return
    if arg not in ["BaseModel", "User"]:
      print("** class doesn't exist **")
      return
    new_instance = eval(arg)()
    new_instance.save()
    print(new_instance.id)

  def do_show(self, arg):
    """Prints the string representation of an instance based on the class name and id"""
    args = arg.split()
    if len(args) == 0:
      print("** class name missing **")
      return
    if args[0] not in ["BaseModel", "User"]:
      print("** class doesn't exist **")
      return
    if len(args) < 2:
      print("** instance id missing **")
      return
    key = args[0] + "." + args[1]
    all_objs = storage.all()
    obj = all_objs.get(key)
    if not obj:
      print("** no instance found **")
    else:
      print(f"{obj.__class__.__name__} {obj}")

  def do_destroy(self, arg):
    """Deletes an instance based on the class name and id"""
    args = arg.split()
    if len(args) == 0:
      print("** class name missing **")
      return
    if args[0] not in ["BaseModel", "User"]:
      print("** class doesn't exist **")
      return
    if len(args) < 2:
      print("** instance id missing **")
      return
    key = args[0] + "." + args[1]
    all_objs = storage.all()
    obj = all_objs.get(key)
    if not obj:
      print("** no instance found **")
    else:
      del all_objs[key]
      storage.save()

  def do_all(self, arg):
    """Prints all string representation of all instances based or not on the class name"""
    args = arg.split()
    all_objs = storage.all()
    if not args:
      print([f"{obj.__class__.__name__} {obj}" for obj in all_objs.values()])
      return
    if args[0] not in ["BaseModel", "User"]:
      print("** class doesn't exist **")
      return
    print([f"{obj.__class__.__name__} {obj}" for obj in all_objs.values() if obj.__class__.__name__ == args[0]])

  def do_update(self, arg):
    """Updates an instance based on the class name and id by adding or updating attribute"""
    args = arg.split()
    if len(args) == 0:
      print("** class name missing **")
      return
    if args[0] not in ["BaseModel", "User"]:
      print("** class doesn't exist **")
      return
    if len(args) < 2:
      print("** instance id missing **")
      return
    key = args[0] + "." + args[1]
    all_objs = storage.all()
    obj = all_objs.get(key)
    if not obj:
      print("** no instance found **")
      return
    if len(args) < 3:
      print("** attribute name missing **")
      return
    if len(args
