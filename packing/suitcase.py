from packing.item_with_holding_capacity import ItemWithHoldingCapacity

class Suitcase(ItemWithHoldingCapacity):
    def __init__(self, max_weight):
        super().__init__(max_weight)
        # ItemsWithHoldingCapacity already has everything we need for suitcases
