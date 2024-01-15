#!/usr/bin/python3
import json
from os import path

""" Base model Class """


class FileStorage():

    __file_path = "file.json"
    __objects   = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                js = json.load(f)
            for key in json_data:
                self.__objects[key] = classes[js[key]["__class__"]](**js[key])


