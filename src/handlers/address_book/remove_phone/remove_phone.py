from src.utils.decorators.input_error import input_error
from src.models.address_book.address_book import AddressBook

@input_error
def remove_phone(args, book: AddressBook):
    if len(args) != 2:
        raise IndexError
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found"
    else:
        record.remove_phone(phone)
        return f"Phone number {phone} for contact {name} removed"