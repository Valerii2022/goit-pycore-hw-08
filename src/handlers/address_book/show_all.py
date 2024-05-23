from src.utils import input_error
from src.models import AddressBook
from colorama import Fore, Style

@input_error
def show_all(args, book: AddressBook):
    if len(args) > 0:
        raise IndexError
    if len(book) == 0:
        return Fore.LIGHTRED_EX + "You have no contacts yet."
    else:
        records = []
        for _, record in book.data.items():
            records.append(str(record))
        return records
        # return book