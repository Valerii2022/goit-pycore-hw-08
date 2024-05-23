from src.utils import input_error
from src.models import AddressBook
from colorama import Fore

@input_error
def change_contact(args, book: AddressBook):
    if len(args) != 3:
        raise IndexError
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return Fore.GREEN + f"Phone number for contact {name} changed"
    else:
        return Fore.RED + f"Contact {name} not found"