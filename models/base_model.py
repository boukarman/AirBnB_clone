#!/usr/bin/python3
from datetime import datetime
import uuid
import models

"""
BaseModel that defines all common
attributes/methods for other classes
"""


class BaseModel:
    """
    public attributes and methods
    should print: [<class name>] (<self.id>) <self.__dict__>

    """
    def __init__(self, *args, **kwargs):
        """
        initialization method
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            models.storage.new(self)  # create new instance on storage file

        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)

                if (key != "__class__"):
                    setattr(self, key, value)

    def __str__(self):
        """
        return the string represintation of BaseModel
        """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

        models.storage.save()  # to storage file

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = \
            my_dict['created_at'].isoformat(timespec='microseconds')
        my_dict['updated_at'] = \
            my_dict['updated_at'].isoformat(timespec='microseconds')

        return my_dict
