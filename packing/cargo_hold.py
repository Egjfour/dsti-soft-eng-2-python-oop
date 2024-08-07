from packing.suitcase import Suitcase

class CargoHold(Suitcase):
    def __init__(self, max_weight): # unsure why this is necessary, but linting is upset -- pylint: disable=W0246
        super().__init__(max_weight)
        # We can recycle the items list from Suitcase to represent the suitcases in a cargo hold, so no need to create a separate list

    def add_suitcase(self, suitcase: Suitcase):
        self.add_item(suitcase) # CargoHolds are Suitcases through inheritance, so we can recycle the add_item method from Suitcase

    def __str__(self):
        # Our str method can be recycled from Suitcase, but we need to replace "item" with "suitcase" to make it make sense
        # Then we just need to replace the second half of the string with the remaining space in the cargo hold instead of the current weight
        return Suitcase.__str__(self).replace("item", "suitcase").split(",")[0] + f" space for {self.max_weight - self._weight} kg"
    
    def print_items(self):
        # We can recycle the print_items method from Suitcase, but we need to iterate through the suitcases
        # to then loop through the items in each suitcase by making a call to the print_items method of Suitcase
        for suitcase in self._items: # Remember that _items is a list of Suitcases for this class
            suitcase.print_items()
