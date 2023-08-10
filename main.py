from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    record_name = 'name'
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone


class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []
    
    
    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        self.phones.append(phone)
    
    
    def remove_phone(self, phone_value):
        self.phones = [phone for phone in self.phones if phone.value != phone_value]
    
    
    def edit_phone(self, old_value, new_value):
        for phone in self.phones:
            if phone.value == old_value:
                phone.value = new_value


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record