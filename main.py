from packing.item import Item
from packing.suitcase import Suitcase

def validate_part_1():
    print("------------ RUNNING TESTS (Part 1) ------------")
    # Create two item instances
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)

    # Print the attributes of the instances using our custom getter methods
    print("Name of the book:", book.name())
    print("Weight of the book:", book.weight())

    assert book.name() == "ABC Book"
    assert book.weight() == 2

    # Print the user-facing string representation of the instances using the overridden __str__ method
    print("Book:", book)
    print("Phone:", phone)

    assert str(book) == "{} ({} kg)".format("ABC Book", 2)

    # Prove that the attributes are protected by trying to update them
    try:
        book.weight = 10
    except AttributeError as e:
        print("Error:", e, "- Cannot update weight after initialization as expected.")
    assert book.weight() == 2
    print("------------ ALL TESTS PASSED (Part 1) ------------")
    return True

def validate_part_2():
    print("------------ RUNNING TESTS (Part 2) ------------")
    # Create some items and a suitcase
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(5)

    # Check that we initialized correctly using inheritance from Item
    assert suitcase._weight == 0 # pylint: disable=W0212
    assert suitcase.max_weight == 5
    print(suitcase)

    for item in [book, phone, brick]:
        suitcase.add_item(item)
        print(suitcase)

    # Check that the suitcase has the correct number of items
    assert len(suitcase._items) == 2 # pylint: disable=W0212

    print("------------ ALL TESTS PASSED (Part 2) ------------")
    return True

def validate_part_3():
    print("------------ RUNNING TESTS (Part 3) ------------")
    # Create some items and a suitcase
    book = Item("ABC Book", 2)

    suitcase = Suitcase(5)
    suitcase.add_item(book)

    print(suitcase)
    assert str(suitcase) == "1 item (2 kg)"

    print("------------ ALL TESTS PASSED (Part 3) ------------")
    return True

def validate_part_4():
    print("------------ RUNNING TESTS (Part 4) ------------")
    # Create some items and a suitcase
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    # Print the items in the suitcase as well as the weight of the suitcase
    suitcase.print_items()
    assert suitcase.print_items() == None

    combined_weight_manual = sum([book.weight(), phone.weight(), brick.weight()])
    combined_weight = suitcase.weight()
    print("Combined weight:", combined_weight, "kg")
    assert combined_weight == combined_weight_manual

    print("------------ ALL TESTS PASSED (Part 4) ------------")
    return True

def validate_part_5():
    print("------------ RUNNING TESTS (Part 5) ------------")
    # Create some items and a suitcase
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    # Print the heaviest item in the suitcase
    print("The headiest item:", suitcase.heaviest_item())
    assert suitcase.heaviest_item() == brick

    print("------------ ALL TESTS PASSED (Part 5) ------------")
    return True

if __name__ == '__main__':
    assert validate_part_1()
    assert validate_part_2()
    assert validate_part_3()
    assert validate_part_4()
    assert validate_part_5()
