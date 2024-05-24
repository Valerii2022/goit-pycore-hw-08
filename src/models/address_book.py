from collections import UserDict
from datetime import datetime, timedelta
from tabulate import tabulate

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            raise ValueError("Record not found.")
        
    def get_upcoming_birthdays(self, days):
        headers = ["Name", "Congratulation date"]
        current_date = datetime.today().date()
        current_timedelta = current_date + timedelta(days)
        current_year = datetime.now().year
        result = []
        for contact in self.data.values():
            if contact.birthday:
                birthday_date = contact.birthday.value.date().replace(year=current_year)
                if birthday_date < current_date:
                    birthday_date = birthday_date.replace(year=current_year + 1)
                if current_date <= birthday_date <= current_timedelta:
                    row =[contact.name, birthday_date.strftime("%d.%m.%Y")]
                    result.append(row)
        result.sort(key=lambda x: datetime.strptime(x[1], "%d.%m.%Y"))
        if len(result) == 0:
            return None
        return tabulate(result, headers, tablefmt="grid")
    
    def __str__(self):
        headers = ["Name", "Birthday",  "Phones" ]
        table = []
        for record in self.data.values():
            row = [
                record.name,
                record.birthday if record.birthday else "",
                record.phones if record.phones else ""
            ]
            table.append(row)
        if len(table) == 0:
            return None
        return tabulate(table, headers, tablefmt="grid")

    def __repr__(self):
        return f"ContactBook: {self.data}"