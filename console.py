#!/usr/bin/python3
"""Module for console."""
import sys
import json
from datetime import datetime
from models.base_model import BaseModel

class_dict = {"BaseModel": BaseModel}

def create(class_name):
    """Create an instance of BaseModel."""
    if class_name == "":
        print("** class name missing **")
        return
    elif class_name not in class_dict:
        print("** class doesn't exist **")
        return
    instance = class_dict[class_name]()
    instance.save()
    print(instance.id)

def show(class_name, obj_id):
    """Show the string representation of an instance."""
    if class_name == "":
        print("** class name missing **")
        return
    elif class_name not in class_dict:
        print("** class doesn't exist **")
        return
    if obj_id == "":
        print("** instance id missing **")
        return
    key = class_name + "." + obj_id
    if key not in BaseModel.__objects:
        print("** no instance found **")
        return
    print(BaseModel.__objects[key])

def destroy(class_name, obj_id):
    """Destroy an instance based on the class name and id."""
    if class_name == "":
        print("** class name missing **")
        return
    elif class_name not in class_dict:
        print("** class doesn't exist **")
        return
    if obj_id == "":
        print("** instance id missing **")
        return
    key = class_name + "." + obj_id
    if key not in BaseModel.__objects:
        print("** no instance found **")
        return
    del BaseModel.__objects[key]
    BaseModel.save_to_file()

def all_instances(class_name):
    """Print all string representations of instances."""
    if class_name == "":
        print("** class name missing **")
        return
    elif class_name not in class_dict:
        print("** class doesn't exist **")
        return
    instances = []
    for key, value in BaseModel.__objects.items():
        if key.split(".")[0] == class_name:
            instances.append(str(value))
    print(instances)

def update(class_name, obj_id, attr_name, attr_value):
    """Update an instance based on the class name and id."""
    if class_name == "":
        print("** class name missing **")
        return
    elif class_name not in class_dict:
        print("** class doesn't exist **")
        return
    if obj_id == "":
        print("** instance id missing **")
        return
    key = class_name + "." + obj_id
    if key not in BaseModel.__objects:
        print("** no instance found **")
        return
    obj = BaseModel.__objects[key]
    if hasattr(obj, attr_name):
        attr_type = type(getattr(obj, attr_name))
        setattr(obj, attr_name, attr_type(attr_value))
        obj.save()
    else:
        print("** attribute name missing **")

if __name__ == "__main__":
    commands = {
        "create": create,
        "show": show,
        "destroy": destroy,
        "all": all_instances,
        "update": update
    }
    if len(sys.argv) < 2:
        sys.exit("Usage: ./console.py <command>")
    command = sys.argv[1]
    if command not in commands:
        sys.exit(f"Unknown command: {command}")
    commands[command](*sys.argv[2:])
