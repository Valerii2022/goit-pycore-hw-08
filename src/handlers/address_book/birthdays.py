from src.utils import input_error
from src.models import AddressBook
from colorama import Fore, Style

@input_error
def birthdays(args, book: AddressBook):
    if len(args) > 1:
        raise IndexError
    if len(book) == 0:
        return Fore.LIGHTRED_EX + "You have no contacts yet." 
    else:
        days, *_ = args
        birthdays = book.get_upcoming_birthdays(int(days))
        if birthdays:
            return birthdays
        else:
            return Fore.LIGHTMAGENTA_EX + "No birthdays next week." 