#!/usr/bin/python3

import uuid
from datetime import datetime

""" Base model Class """


class BaseModel():

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def __str__(self):
        id = self.id
        dict = self.__dict__
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, id, dict)

    def to_dict(self):
        """Returns a dictionary representation of the object"""
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value

        return obj_dict
