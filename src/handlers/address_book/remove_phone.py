from src.utils import input_error
from src.models import AddressBook

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