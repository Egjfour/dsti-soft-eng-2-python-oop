from packing.classes import Item, Suitcase, CargoHold #pylint: disable=W0611

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
    print("The heaviest item:", suitcase.heaviest_item())
    assert suitcase.heaviest_item() == brick

    print("------------ ALL TESTS PASSED (Part 5) ------------")
    return True

def validate_part_6():
    print("------------ RUNNING TESTS (Part 6) ------------")
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)
    print("Ada's Suitcase:", adas_suitcase)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)
    print("Peter's Suitcase:", peters_suitcase)

    cargo_hold = CargoHold(1000)
    # Validate initialization
    assert cargo_hold.max_weight == 1000
    assert len(cargo_hold._items) == 0 # pylint: disable=W0212
    assert cargo_hold.weight() == 0 # pylint: disable=W0212
    print(cargo_hold)
    assert 'space for 1000 kg' in str(cargo_hold)

    cargo_hold.add_suitcase(adas_suitcase)
    assert cargo_hold.weight() == adas_suitcase.weight()
    assert len(cargo_hold._items) == 1 # pylint: disable=W0212
    print(cargo_hold)
    assert 'space for 997 kg' in str(cargo_hold)

    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)
    assert 'space for 993 kg' in str(cargo_hold)

    print("------------ ALL TESTS PASSED (Part 6) ------------")
    return True

def validate_part_7():
    print("------------ RUNNING TESTS (Part 7) ------------")
    # Create some items and a suitcase
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)
    print("Ada's Suitcase:", adas_suitcase)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)
    print("Peter's Suitcase:", peters_suitcase)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    # Print the items in the cargo hold
    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()

    print("------------ ALL TESTS PASSED (Part 7) ------------")
    return True

if __name__ == '__main__':
    assert validate_part_1()
    print("\n\n")

    assert validate_part_2()
    print("\n\n")

    assert validate_part_3()
    print("\n\n")

    assert validate_part_4()
    print("\n\n")

    assert validate_part_5()
    print("\n\n")

    assert validate_part_6()
    print("\n\n")

    assert validate_part_7()
    print("------------ ALL TESTS PASSED ------------")
