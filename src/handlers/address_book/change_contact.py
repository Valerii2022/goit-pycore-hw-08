from src.utils.decorators.input_error import input_error
from src.models.address_book import AddressBook

@input_error
def change_contact(args, book: AddressBook):
    if len(args) != 3:
        raise IndexError
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return f"Phone number for contact {name} changed"
    else:
        return f"Contact {name} not found"