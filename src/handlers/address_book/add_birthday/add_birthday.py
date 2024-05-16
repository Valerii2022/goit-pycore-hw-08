from src.utils.decorators.input_error import input_error
from src.models.address_book.address_book import AddressBook

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        raise IndexError
    name, birthday, *_ = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday for contact {name} changed"
    else:
        return f"Contact {name} not found"