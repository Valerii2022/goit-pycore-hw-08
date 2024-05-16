from collections import UserDict
from datetime import datetime, timedelta

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
        
    def get_upcoming_birthdays(self):
        current_date = datetime.today().date()
        current_timedelta = current_date + timedelta(7)
        current_year = datetime.now().year
        result = []
        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.value.date().replace(year=current_year)
                if birthday_date < current_date:
                    birthday_date = birthday_date.replace(year=current_year + 1)
                if current_date <= birthday_date <= current_timedelta:
                    result.append({"name": record.name.value, "congratulation_date": birthday_date.strftime("%d.%m.%Y")})
        result.sort(key=lambda x: x["congratulation_date"])
        return result