from src.utils.decorators.input_error import input_error
from src.models.address_book.address_book import AddressBook
from src.models.record.record import Record

@input_error
def add_contact(args, book: AddressBook):
    if len(args) != 2:
        raise IndexError
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        try:
            record.add_phone(phone)
        except:
            raise ValueError("The phone number must consist of 10 digits")
    return message

