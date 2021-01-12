PAIR_COMMAND = "Paid"
END_COMMAND = "End"
names = []
input_line = input()

while not input_line == END_COMMAND:
    if input_line == PAIR_COMMAND:
        for name in names:
            print(name)
        names = []
    if input_line != PAIR_COMMAND:
        names.append(input_line)
    input_line = input()

print(f"{len(names)} people remaining.")