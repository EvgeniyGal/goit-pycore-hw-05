from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Please provide a valid name and phone number."
        except IndexError:
            return "Error: Missing arguments."
        except Exception as e:
            return f"Unexpected error: {e}"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Command 'add' requires exactly 2 arguments.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Command 'change' requires exactly 2 arguments.")
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError(f"Contact '{name}' not found.")


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Command 'phone' requires exactly 1 argument.")
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        raise KeyError(f"Contact '{name}' not found.")


@input_error
def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
