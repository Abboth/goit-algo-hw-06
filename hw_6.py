from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if re.match(r"\+?\d{2}?\d{10}$", value):
            super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(phone)

    def remove_phone(self, phone: str) -> str:
        try:
            for phone_number in self.phones:
                if phone_number == phone:
                    self.phones.remove(phone_number)
        except ValueError:
            print("Incorrect number")

    def edit_phone(self, old_phone: str, new_phone: str):
        if old_phone in self.phones:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)

    def find_phone(self, phone: str) -> str:
        if phone in self.phones:
            for phone_number in self.phones:
                return phone_number
        else:
            print(f"phone number doesn't exist")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            for key, record in self.data.items():
                if key == name:
                    return record
        else:
            print("phone number is not exist in contacts yet")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print("contact is not exist")

    def __str__(self):
        result = []
        for name, record in self.data.items():
            result.append(str(record))
        return "\n".join(result)


book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
print(book)
