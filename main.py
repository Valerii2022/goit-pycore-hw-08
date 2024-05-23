from src.handlers import add_birthday, add_contact, birthdays, change_contact, show_all, show_phone, remove_phone, show_birthday
from src.utils import load_data, save_data, parse_input
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

commands = [
    "close ", "exit ", "hello ", "add ", "change ", "phone ", "remove-phone ", "all ", "add-birthday ", "show-birthday ", "birthdays ", "help "
]

command_completer = WordCompleter(commands, ignore_case=True)


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = prompt("Enter a command: ", completer=command_completer)
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
                print("Usage: change <contact_name>")
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
        except (EOFError, KeyboardInterrupt):
            save_data(book)
            print("Good bye!")
            break

if __name__ == "__main__":
    main()