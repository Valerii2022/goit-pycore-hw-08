from src.utils.decorators.input_error import input_error
from src.models.address_book.address_book import AddressBook

@input_error
def show_phone(args, book: AddressBook):
    if len(args) != 1:
        raise IndexError
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found"
    else:
        finded_phone = record.find_phone()
        if finded_phone:
            return finded_phone
        else:
            return f"No phones for contact {name}"