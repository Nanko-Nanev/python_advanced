input_string = input()

open_brackets = []

for i in range(len(input_string)):
    ch = input_string[i]
    if ch == "(":
        open_brackets.append(i)
    elif ch == ")":
        last_open_brackets = open_brackets.pop()
        print(input_string[last_open_brackets:i + 1])
