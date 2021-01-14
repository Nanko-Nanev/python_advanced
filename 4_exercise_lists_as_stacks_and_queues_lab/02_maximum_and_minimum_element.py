from collections import deque

n = int(input())
my_stack = deque()

for i in range(n):
    input_command = input().split()
    if input_command[0] == "1":
        my_stack.append(input_command[1])
    elif input_command[0] == "2":
        if my_stack:
            my_stack.pop()
    elif input_command[0] == "3":
        if my_stack:
            temp = [int(el) for el in my_stack]
            print(max(temp))
    elif input_command[0] == "4":
        if my_stack:
            temp_m = [int(el) for el in my_stack]
            print(min(temp_m))
    else:
        pass

result = []
while my_stack:
    result.append(my_stack.pop())
result = [str(el) for el in result]

print(", ".join(result))