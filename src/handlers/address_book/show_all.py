from src.utils.decorators.input_error import input_error
from src.models.address_book import AddressBook

@input_error
def show_all(args, book: AddressBook):
    if len(args) > 0:
        raise IndexError
    if len(book) == 0:
        return "You have no contacts yet."   
    else:
        records = []
        for _, record in book.data.items():
            records.append(str(record))
        return records