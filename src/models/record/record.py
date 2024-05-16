from src.models.name.name import Name
from src.models.phone.phone import Phone
from src.models.birthday.birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for record_phone in self.phones:
            if str(record_phone) == phone:
                self.phones.remove(record_phone)
                return 
        raise ValueError("Phone number not found")

    def edit_phone(self, old_phone, new_phone):
        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("The phone number must consist of 10 digits")
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone
                return
        raise ValueError("Phone number not found")

    def find_phone(self):
        phones = '; '.join(p.value for p in self.phones)
        return phones
    
    def show_birthday(self):
        return self.birthday

    def __str__(self):
        birthday = self.birthday if self.birthday else 'not provided'
        phones ='; '.join(p.value for p in self.phones) if self.phones else'not provided'
        return f"Contact name: {self.name.value}, birthday: {birthday}, phones: {phones}"