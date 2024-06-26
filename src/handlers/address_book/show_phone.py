from src.utils import input_error
from src.models import AddressBook

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
            return f"Phones for contact {name}: {finded_phone}"
        else:
            return f"No phones for contact {name}"