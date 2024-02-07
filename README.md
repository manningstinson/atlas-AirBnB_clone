# Atlas School - airbnb clone

![airbnb clone](https://github.com/manningstinson/atlas-AirBnB_clone/assets/104523090/2293c7ad-a821-417a-8acb-dc2c6961d06b)

In this six part project, two team members are creating a clone of the airbnb travel website. The first project will be a console, or shell to access the project from the terminal/command line.

## Authors

This project is a a collaborative effort between the below authors. You can learn more about the authors by visiting their github profiles through the links below.

[Manning Stinson](https://github.com/manningstinson) |
[Brandon Montezuma](https://github.com/bmontezuma)

## How to start the project

## How to use it

## Command Interpreter

A command interpreter is a tool that allows you to interact with your project by entering commands. It's like a specialized interface where you can perform actions such as creating new users or places, retrieving objects, performing operations on objects, updating attributes, and destroying objects.

If you want to create a new user, you could use the following:

```python
create User
```

or if you want to retrieve objects you could use the following:
```Python
def retrieve_objects(self, obj_type):
    if obj_type in self.objects:
        print(f"Retrieving {obj_type}:")
        for obj in self.objects[obj_type]:
            print(obj.name)
```
```def retrieve_objects(self, obj_type):```: This line defines a method called retrieve_objects within a class. The method takes two parameters: ```self```, which represents the instance of the class, and ```obj_type```, which is the type of object the method is meant to retrieve.

if ```obj_type in self.objects:```: This line checks if the specified ```obj_type``` exists in the ```self.objects``` dictionary. ```self.objects``` is assumed to be a dictionary where keys represent object types, and values are lists of objects of that type.

```print(f"Retrieving {obj_type}:")```: If the ```obj_type``` exists in the dictionary, this line prints a message indicating that objects of that type are being retrieved.

for ```obj in self.objects[obj_type]:```: This line iterates over the list of objects associated with the obj_type in the self.objects dictionary.

```print(obj.name)```: Within the loop, this line prints the name attribute of each object. It assumes that the objects have a name attribute that holds information identifying the object. 
For instance, if ```obj_type is 'users'```, this line would print the name of each user object retrieved.

Overall, this method retrieves objects of a specified type (obj_type) from the ```self.objects``` dictionary and prints out their names or relevant information. If the specified type does not exist in the dictionary, it prints a message indicating that no such objects were found.



## Full Project Documentation

This project will be fully documented at the airbnb clone wiki. You can access it here:
[airbnb-clone-wiki](https://github.com/manningstinson/atlas-AirBnB_clone/wiki/Home-%7C-airbnb-clone)
