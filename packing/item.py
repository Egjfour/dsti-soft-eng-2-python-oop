  
"""
This file contains the item class definition and methods.
"""

class Item(object):
    # Only allow protected attributes _name and _weight to be set
    __slots__ = ['_name', '_weight']

    def __init__(self, name, weight):
        self.__set_name(name)
        self.__set_weight(weight)

    # Weight getter and setter (private so we cannot update after initialization)
    # Would normally use the @property decorator, 
    # but that does not fully encapsulate the attributes such that instance.x = y is still possible
    def __set_weight(self, weight):
        if weight < 0:
            raise ValueError("Weight must be non-negative.")
        self._weight = weight

    def __get_weight(self):
        return self._weight
    
    def weight(self):
        # Custom getter that will allow us to call item.weight() instead of item.weight
        return self.__get_weight()

    # Name getter and setter (same rationale as weight)
    def __set_name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty.")
        self._name = name

    def __get_name(self):
        return self._name

    def name(self):
        # Customer getter. Same as the one for weight
        return self.__get_name()

    def __str__(self):
        return "{} ({} kg)".format(self._name, self._weight)
