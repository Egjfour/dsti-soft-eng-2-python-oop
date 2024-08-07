from packing.item import Item

class Suitcase(Item):
    __slots__ = ['_items', '_max_weight', '__total_weight']

    def __init__(self, max_weight):
        super().__init__("Suitcase", 0)
        self._items = []
        self.max_weight = max_weight

    @property
    def max_weight(self):
        return self._max_weight
    
    @max_weight.setter
    def max_weight(self, max_weight):
        if max_weight <= 0:
            raise ValueError("Max weight must be a positive number")
        self._max_weight = max_weight

    def add_item(self, item: Item):
        if self.weight() + item.weight() > self.max_weight:
            print(f"Item {item.name()} with weight {item.weight()} kg. is too heavy to add to suitcase. " +
                  f"Current total weight is {self.weight()} kg.")
            return False
        self._items.append(item)
        self._weight = self.weight() + item.weight() # pylint: disable=W0201
        return True
    
    def __str__(self):
        total_item_count = len(self._items)
        total_weight = self.weight()

        # Handle the special case where the suitcase has only one item (English grammar)
        return f"{total_item_count} item{'s' if total_item_count != 1 else ''} ({total_weight} kg)"

    def print_items(self):
        for item in self._items:
            print(item)

    def heaviest_item(self):
        # In case the suitcase is empty, return None
        if len(self._items) == 0:
            return None
        
        # Return the item with the highest weight using a lambda function inside of max
        return max(self._items, key=lambda item: item.weight())
