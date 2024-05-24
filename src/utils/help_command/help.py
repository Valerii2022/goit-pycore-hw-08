from ..decorators.input_error import input_error
from tabulate import tabulate

commands1 = [
    "close", "exit", "hello", "change", "phone", "remove-phone", "all", "show-birthday", "birthdays", "help"
]

commands = [{"command": "add", "description": "add new contact", "number": 2, "arguments_description":"<name> - contact name, <phone> - contact phone number, must consist of 10 digits"}, {"command": "add-birthday", "description": "add contact birthday", "number": 2, "arguments_description":"<name> - contact name, <birthday> - contact birthday, use format DD.MM.YYYY"}]

@input_error
def help():
    headers = ['Command', 'Command description', 'Number of arguments', 'Arguments description']
    table = []
    for command in commands:
        row = [command['command'], command['description'], command['number'], command['arguments_description']]
        table.append(row)
    return tabulate(table, headers, tablefmt="grid")
