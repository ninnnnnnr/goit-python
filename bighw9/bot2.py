vr = ''
dict_user = {}
users = []


def input_error(func):
    def wrapper(*args, **kwargs):
        ret = 0
        try:
            ret = func(*args, **kwargs)
        except ValueError:
            print('>> Enter true name and phone')
            main()
        except Exception:
            print('>> Enter true name command')
            main()
        return ret
    return wrapper

@input_error
def add_handler(command):
    vr = input('Name and phone:')
    vr = vr.split(' ')
    dict_user = dict([vr])
    users.append(dict_user)
    print('Ok')

@input_error
def change_handler(command):
    if len(users) == 0:
        print('list contacts empty')
    vr = input(f'For change input name and phone:')
    vr = vr.split(' ')
    # где-то здесь нужно вставить try
    for i in users:
        if vr[0] in i:
            iii = {vr[0]: vr[1]}
            i.update(iii)
            print(users)
        else:
            print('no name in contacts')

@input_error
def phone_handler(command):
    vr = input(f'For search input name:')
    for i in users:
        if vr in i:
            print(f'phone number:{i.get(vr)}')

@input_error
def hello_handler(command):
    return "How can I help you?"

@input_error
def showall_handler(command):
    return users

@input_error
def bye_handler(command):
    return "Good bye!"

@input_error
def main():
    while True:
        command = input('Hello, your command ?:')
        list_of_command = ["Good bye!", 'hello', 'add', 'change', 'phone', 'show all',"close", "exit","."]
        if len(command) < 0 or command not in list_of_command:
            raise Exception
        command = command.lower()
        if 'hello' in command:
            hello_handler(command)
        elif 'add' in command:
            add_handler(command)
        elif 'change' in command:
            change_handler(command)
        elif 'phone' in command:
            phone_handler(command)
        elif 'show all' in command:
            showall_handler(command)
        elif "good bye" or "close" or "exit" or "." in command:
            bye_handler(command)
            break


if __name__ == '__main__':
    main()
