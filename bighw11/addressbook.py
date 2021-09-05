import re
from collections import UserDict
from datetime import datetime


class IncorrectInput(Exception):
    pass


class AddressBook(UserDict):
    def add(self, record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
        else:
            self.data[record.name.value].add_phones(record.phones)

    def edit_record(self, old_record, new_record):
        if old_record.name.value not in self.data:
            return
        self.data[old_record.name.value].update_phone(
            old_record.phones[0], new_record.phones[0]
        )

    def delete(self, record):
        if record.name.value in self.data:
            self.data.pop(record.name.value)

    def phone(self, record):
        if record.name.value in self.data.keys():
            return self.data[record.name.value]

    def __str__(self):
        return "\n".join([
            str(record) for record in self.data.values()
        ])

    def iterator(self, item_number):
        counter = 0
        result = ""
        for name, record in self.data.items():
            result += str(record) + "\n"
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ""
        yield result


class Record:
    def __init__(self, name, phones=None, birthday=None):
        self.name = name
        self.birthday = birthday
        if phones is None:
            self.phones = []
        else:
            self.phones = phones

    def __repr__(self):
        result = f"{str(self.name)}\n{20 * '='}"
        for idx, phone in enumerate(self.phones, start=1):
            result += f"\n{idx} {phone}"
        return result

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def add_phones(self, phone_numbers):
        self.phones.extend(phone_numbers)

    def update_phone(self, old_phone, new_phone):
        index = 0
        for idx, phone in enumerate(self.phones):
            if str(phone) == str(old_phone):
                index = idx
                break
        self.phones[index] = new_phone

    def days_to_birthday(self):
        if not self.birthday:
            return
        now = datetime.today()
        if (self.birthday.value.replace(year=now.year) - now).days > 0:
            return (self.birthday.value.replace(year=now.year) - now).days
        return (self.birthday.value.replace(year=now.year + 1) - now).days


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return f"{self.__class__.__name__}: {self.value}"


class Name(Field):
    pass


class Phone(Field):
    PHONE_REGEX = re.compile(r"^\+?(\d{2})?\(?(0\d{2})\)?(\d{7}$)")

    def __init__(self, value):
        super().__init__(value)
        self.country_code = ""
        self.operator_code = ""
        self.phone_number = ""

    def __repr__(self):
        return self.value

    @Field.value.setter
    def value(self, value: str):
        value = value.replace(" ", "")
        search = re.search(self.PHONE_REGEX, value)
        try:
            country, operator, phone = search.group(1, 2, 3)
        except AttributeError:
            raise IncorrectInput(f"No phone number found in {value}")

        if operator is None:
            raise IncorrectInput(f"Operator code not found in {value}")

        self.country_code = country if country is not None else "38"
        self.operator_code = operator
        self.phone_number = phone
        self.__value = f"+{self.country_code}({self.operator_code}){self.phone_number}"


class Birthday(Field):
    @Field.value.setter
    def value(self, value: str):
        self.__value = datetime.strptime(value, '%d%m%Y').date()
