from packing.item import Item

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

if __name__ == '__main__':
    assert validate_part_1()
