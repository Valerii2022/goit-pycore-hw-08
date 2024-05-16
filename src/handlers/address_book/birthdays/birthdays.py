from src.utils.decorators.input_error import input_error
from src.models.address_book.address_book import AddressBook

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