from src.utils.decorators.input_error import input_error
from src.models.address_book.address_book import AddressBook

@input_error
def show_birthday(args, book: AddressBook):
    if len(args) != 1:
        raise IndexError
    name, *_ = args
    record = book.find(name)
    if record:
        birthday = record.show_birthday()
        if birthday:
            return f"Birthday for contact {name}: {birthday}"
        else:
            return f"Birthday for contact {name} not provided"
    else:
        return f"Contact {name} not found"