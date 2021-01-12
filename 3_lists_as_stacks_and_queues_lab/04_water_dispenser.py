from collections import deque

START_COMMAND = "Start"
REFILL_COMMAND = "refill"
END_COMMAND = "End"
names = deque()

quantity = int(input())
input_command = input()

while not input_command == START_COMMAND:
    names.append(input_command)
    input_command = input()

input_liters = input().split()
while True:
    if input_liters[0] == REFILL_COMMAND:
        quantity += int(input_liters[1])
    elif input_liters[0] == END_COMMAND:
        break
    else:
        if quantity >= int(input_liters[0]):
            print(f"{names.popleft()} got water")
            quantity -= int(input_liters[0])
        else:
            print(f"{names.popleft()} must wait")

    input_liters = input().split()

print(f"{quantity} liters left")