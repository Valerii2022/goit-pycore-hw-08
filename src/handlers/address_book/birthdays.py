from src.utils import input_error
from src.models import AddressBook

@input_error
def birthdays(args, book: AddressBook):
    if len(args) > 0:
        raise IndexError
    if len(book) == 0:
        return "You have no contacts yet."   
    else:
        birthdays = book.get_upcoming_birthdays()
        if birthdays:
            return birthdays
        else:
            return "No birthdays next week."