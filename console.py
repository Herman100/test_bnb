#!/usr/bin/python3
"""a custom cmd module that contains the
entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in ["BaseModel", "User", "State", "City",
                         "Place", "Amenity", "Review"]:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on its ID"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on its ID"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key in instances:
                instance = instances[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')
                try:
                    attr_type = type(getattr(instance, attr_name))
                    attr_value = attr_type(attr_value)
                except AttributeError:
                    pass
                setattr(instance, attr_name, attr_value)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances"""
        args = arg.split()
        instances = storage.all()
        if len(args) == 0:
            print([str(value) for value in instances.values()])
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            print([str(value) for value in instances.values()
                  if value.__class__.__name__ == args[0]])

    def default(self, line):
        """Method called on an input line when
        the command prefix is not recognized"""
        args = line.split('.')
        if len(args) == 2:
            class_name = args[0]
            command = args[1]
            if command == "all()":
                self.do_all(class_name)
            elif command == "count()":
                self.do_count(class_name)
            elif command.startswith("show(") and command.endswith(")"):
                instance_id = command[5:-1].strip('"')
                self.do_show("{} {}".format(class_name, instance_id))
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_count(self, arg):
        """Prints the number of instances of a class"""
        args = arg.split()
        instances = storage.all()
        if len(args) == 0:
            print(len(instances))
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            count = len([value for value in instances.values()
                         if value.__class__.__name__ == args[0]])
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
