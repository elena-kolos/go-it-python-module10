from collections import UserDict


class AddressBook(UserDict):
    def __init__(self, contacts) -> None:
        self.contacts = contacts


ucontacts = AddressBook({})


class Name:
    def __init__(self, name: str) -> None:
        self.name = name


class Phone:
    def __init__(self, phone: str) -> None:
        self.phone = phone


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError):
            return "You should enter command (space) name (space) phone"

    return wrapper


def hello(*args):
    return 'How can I help you?'


def exit(*args):
    return 'Good bye'


@input_error
def add(*args):
    uname = Name(args[0])
    uphone = Phone(args[1])
    ucontacts.contacts[uname.name] = uphone.phone
    # print(ucontacts.contacts)
    return f'contact {uname.name} added successfully'


@input_error
def change(*args):
    uname = Name(args[0])
    uphone_n = Phone(args[1])

    for key in ucontacts.contacts.keys():
        if uname.name == key:
            ucontacts.contacts[uname.name] = uphone_n.phone
            return f'Contact {uname.name} changed successfully'


def get_phone(*args):
    uname = Name(args[0])
    for key in ucontacts.contacts.keys():
        if uname.name == key:
            user_phone = ucontacts.contacts.get(key)
    return user_phone


def show_all(*args):
    return '\n'.join([f'{k}:{v}' for k, v in ucontacts.contacts.items()])
    # lst = ['{:<12}:{:>12}'.format(k, v) for k, v in contacts.items()]
    # return '\n'.join(lst)


# COMM_EXIT=['good bye', 'exit', 'close', '.']
COMMANDS = {exit: ['good bye', 'exit', 'close', '.'], add: ['add', 'додай'], change: [
    'change', 'заміни'], get_phone: ['phone', 'номер'], show_all: ['show all', 'show'], hello: ['hello', 'hi']}


def parse_command(request: str):
    for k, v in COMMANDS.items():
        for i in v:
            if request.lower().startswith(i.lower()):
                return k, request[len(i):].strip().split(' ')


def main():

    while True:
        request = input('You: ')

        result, data = parse_command(request)
        print(result(*data))

        if result is exit:
            break


if __name__ == '__main__':
    main()
