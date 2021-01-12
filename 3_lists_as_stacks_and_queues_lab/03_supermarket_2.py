from collections import deque

END_COMMAND = "End"
PAID_COMMAND = "Paid"

names_queue = deque()

while True:
    input_line = input()
    if input_line == END_COMMAND:
        print(f"{len(names_queue)} people remaining.")
        break
    elif input_line == PAID_COMMAND:
        while names_queue:
            print(names_queue.popleft())
    else:
        names_queue.append(input_line)