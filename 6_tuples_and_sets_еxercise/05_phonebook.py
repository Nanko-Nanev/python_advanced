phonebook = {}
command_input = input()

while not command_input[0].isdigit():
    name, number = command_input.split("-")
    phonebook[name] = number

    command_input = input()

for _ in range(int(command_input)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
