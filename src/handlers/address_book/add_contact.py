from src.utils import input_error
from src.models import AddressBook
from src.models import Record
from colorama import Fore

@input_error
def add_contact(args, book: AddressBook):
    if len(args) != 2:
        raise IndexError
    name, phone, *_ = args
    record = book.find(name)
    message = Fore.GREEN + "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = Fore.GREEN + "Contact added."
    if phone:
        try:
            record.add_phone(phone)
        except:
            raise ValueError("The phone number must consist of 10 digits")
    return message

