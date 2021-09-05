import pickle

from addressbook import Record, AddressBook, Name, Phone

DEFAULT_ADDRESS_BOOK_PATH = ".address_book.bin"

def dump_address_book(path, address_book):
    with open(path, "wb") as f:
        pickle.dump(address_book, f)


def load_address_book(path):
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


if __name__ == "__main__":
    list_of_command = ["Good bye!", 'hello', 'add', 'change', 'phone', 'show all', 'birthday', "close", "exit", "."]
    address_book = load_address_book(DEFAULT_ADDRESS_BOOK_PATH)
    while True:
        command = input(f"Hello, your command (hello, add, show all, phone, change, Good bye!, birthday, close, exit, "
                        f".) ?:\n")
        command = command.lower()
        if 'add' in command:
            name = input("Input name contact: ")
            phone = input("Input phone contact: ")
            record = Record(Name(name), [Phone(phone)])
            address_book.add(record)
            print('ok')
        elif 'hello' in command:
            print(f"\nHow can I help you? \n{20 * '_'}\nCommands:'Good bye!', 'hello', 'add', 'change', "
                        f"'phone', 'show all'', 'close', 'exit', '.'\n{20 * '_'}\n\n")
        elif "show all" in command:
            for page in address_book.iterator(2):
                print(page)
        elif 'change' in command:
            name = input("Input name contact: ")
            old_phone = input("Input old phone contact: ")
            new_phone = input("Input new phone contact: ")
            old_record = Record(Name(name), [Phone(old_phone)])
            new_record = Record(Name(name), [Phone(new_phone)])
            address_book.edit_record(old_record, new_record)

        elif 'birthday' in command:
            name = input("Input name contact: ")
            birthday = input("Input birthday contact: ")
            rec1 = Record(name, birthday)
            print(rec1.days_to_birthday())

        elif 'delete' in command:
            name = input("Input name contact: ")
            phone = input("Input phone: ")
            record = Record(Name(name), [Phone(phone)])
            address_book.delete(record)
        elif 'phone' in command:
            name = input("Input name contact: ")
            record = Record(Name(name))
            print(address_book.phone(record))
        elif "good bye" in command or "close" in command or "exit" in command or "." in command:
            print("Bye!")
            dump_address_book(DEFAULT_ADDRESS_BOOK_PATH, address_book)
            break
        else:
            print(f"Unrecognized command: {command}")
            print(f"Available commands: {list_of_command}")