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
        if kwargs is not None or kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated-at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
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
        return ("[{}] ({}) {}".format(classname, self.id, self.__dict__))


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
