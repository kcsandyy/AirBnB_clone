#!/usr/bin/python3
"""
A class that defines all common attribute
for other classes
"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates the public instance attribute updated_at

        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary

        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict
    
    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>

        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
