from collections import UserDict


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

    def show_all(self):
        for i in self.data.values():
            if i is None:
                print('')
            else:
                print(i)

    def __str__(self):
        return "\n".join([
            str(record) for record in self.data.values()
        ])


class Record:
    def __init__(self, name, phones=None):
        self.name = name
        if phones is None:
            self.phones = []
        else:
            self.phones = phones

    def __repr__(self):
        result = f"{20 * '_'}\n{str(self.name)}\n"
        for idx, phone in enumerate(self.phones, start=1):
            result += f"{idx} {phone}"
        return result

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def update_phone(self, old_phone, new_phone):
        index = 0
        for idx, phone in enumerate(self.phones):
            if str(phone) == str(old_phone):
                index = idx
                break
        self.phones[index] = new_phone


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

    def __init__(self, value):
        super().__init__(value)

    def __repr__(self):
        return self.value


