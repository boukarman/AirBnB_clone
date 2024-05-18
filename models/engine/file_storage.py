#!/usr/bin/python3
""" FileStorage class definition """
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    hat serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        key = BaseModel.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                dic = json.loads(f.read())
                for value in dic.values():
                    obj = value["__class__"]
                    self.new(eval(obj)(**value))
