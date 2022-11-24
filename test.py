#!/usr/bin/python3
#I want to create a class called BaseModel
import uuid

class BaseModel():
    #now i am creatin instance attributes
    def __init__(self):
        #first(public)is the id: using uuid4
        self.id = str(uuid.uuid4())
