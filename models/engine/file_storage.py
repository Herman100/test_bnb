#!/usr/bin/python3
""""This modules defines the file storage class for json file"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                class_name = value["__class__"]
                if class_name in ["BaseModel", "User"]:
                    FileStorage.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
