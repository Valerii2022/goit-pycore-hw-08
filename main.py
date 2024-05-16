from src.handlers.address_book.add_birthday.add_birthday import add_birthday
from src.handlers.address_book.add_contact.add_contact import add_contact
from src.handlers.address_book.birthdays.birthdays import birthdays
from src.handlers.address_book.change_contact.change_contact import change_contact
from src.handlers.address_book.remove_phone.remove_phone import remove_phone
from src.handlers.address_book.show_all.show_all import show_all
from src.handlers.address_book.show_birthday.show_birthday import show_birthday
from src.handlers.address_book.show_phone.show_phone import show_phone
from src.utils.data.load_data import load_data
from src.utils.data.save_data import save_data
from src.utils.decorators.input_error import input_error
from src.models.address_book.address_book import AddressBook

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    current_book = load_data()
    book = current_book if current_book else AddressBook() 
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))
        
        elif command == "change":
            print(change_contact(args, book))
        
        elif command == "phone":
            print(show_phone(args, book))

        elif command == "remove-phone":
            print(remove_phone(args, book))

        elif command == "all":
            print(show_all(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()