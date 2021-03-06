#Classes and Object-Oriented Programming

#A simple Rectangle class that:
#-Accepts length and width as parameters when creating a new instance
#-Has a perimeter method that returns the perimeter of the rectangle
#-Has an area method that returns the area of the rectangle

class Rectangle:
    def_init_(self)
        self.length = 1
        self.width = 1

    def get_perimeter(self,length,width)
        return self.length * 2 + self.width * 2

    def get_area(self,length,width)
        return self.length * self.width

#A class called Ulist that overrides the __add__, append, and extend methods so that duplicate values are not added to the list by any of these operations.

import UserList

class Ulist(UserList.UserList):
    def __init__(self,data = []):
        UserList.UserList.__init__(self)
        self.data = data

    def __add__(self,value):
        for item in value:
            if item not in self.data:
                self.data += [item]
        return self.data

    def append(self,value):
        if value not in self.data:
            return self.data.append(value)

    def extend(self,value):
        for item in value:
            if item not in self.data:
                return self.data.extend(item)

#A class called Odict, which is just like a dictionary but remembers the order in which key/value pairs are added to the dictionary.

import UserDict

class Odict(UserDict.UserDict):
    def __init__(self,data = {}):
        UserDict.UserDict.__init__(self)
        self.update(data)
        self.keylist = []

    def __setitem__(self,key,value):
        self.data[key] = value
        self.keylist.append(key)

    def okeys(self):
        return self.keylist
