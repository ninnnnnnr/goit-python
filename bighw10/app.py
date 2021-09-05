from addressbook import Record, AddressBook, Name, Phone


if __name__ == "__main__":
    list_of_command = ["Good bye!", 'hello', 'add', 'change', 'phone', 'show all', "close", "exit", "."]
    address_book = AddressBook()
    while True:
        command = input(f"Hello, your command ?:\n")
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
        elif 'show all' in command:
            address_book.show_all()
        elif 'change' in command:
            name = input("Input name contact: ")
            old_phone = input("Input old phone contact: ")
            new_phone = input("Input new phone contact: ")
            old_record = Record(Name(name), [Phone(old_phone)])
            new_record = Record(Name(name), [Phone(new_phone)])
            address_book.edit_record(old_record, new_record)
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
            break
        else:
            print(f"Unrecognized command: {command}")
            print(f"Available commands: {list_of_command}")