#!/usr/bin/python3
#I want to create a class called BaseModel
import uuid
import datetime

class BaseModel():
    #now i am creatin instance attributes
    def __init__(self, *args, **kwargs):
        #first(public)is the id: using uuid4
        self.id = str(uuid.uuid4())
        #the time the instance was created
        self.created_at = datetime.datetime.now()
        #i want the time when the item is updated
        self.updated_at = datetime.datetime.now()
        #i want to work on str
        #done now time for dictionary
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs != 0):
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated-at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = datetime.strptime(value, tform)
    def save(self):
        #i am creating the save method to update time
        self.updated_at = datetime.datetime.now()
    def to_dict(self):
        #returns a dictionary
        d = self.__dict__.copy()
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        d["__class__"] = self.__class__.__name__
        return (d)
    def __str__(self):
        classname = self.__class__.__name__
        return ("[{}] ({}) {}".format(classmame, self.id, self.__dict__))
a = BaseModel()
print(a.created_at)
