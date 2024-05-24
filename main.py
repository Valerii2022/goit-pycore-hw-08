from src.handlers import add_birthday, add_contact, birthdays, change_contact, show_all, show_phone, remove_phone, show_birthday
from src.utils import load_data, save_data, parse_input, help
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from colorama import init, Fore, Style, Back

init()

commands = [
    "close", "exit", "hello","add", "change", "phone", "remove-phone", "all", "add-birthday", "show-birthday", "birthdays", "help"
]

command_completer = WordCompleter(commands, ignore_case=True)


def main():
    book = load_data()
    print(Fore.YELLOW + "Welcome to the assistant bot!")
    while True:
        try:
            user_input = prompt("Enter a command: ", completer=command_completer)
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(book)
                print(Fore.YELLOW + "Good bye!" + Style.RESET_ALL)
                break

            elif command == "help":
                print(help())
                # print(f"{Back.WHITE}add:{Style.RESET_ALL} add new contact, need 2 arguments - name and phone number 10 digits\n{Back.WHITE}change:{Style.RESET_ALL} change contact phone information, need 3 arguments - name, phone wich need to be changed and new phone\n{Back.WHITE}phone:{Style.NORMAL} show contact phones information, need 1 argument - contact name")

            elif command == "hello":
                print(Fore.YELLOW + "How can I help you?" + Style.RESET_ALL)

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
                print(Fore.RED + "Invalid command.")
        except (EOFError, KeyboardInterrupt):
            save_data(book)
            print(Fore.YELLOW + "Good bye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()