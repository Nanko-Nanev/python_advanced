from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
passed_cars = 0

pass_time = green_light + free_window
command = input()
is_crashed = False
is_closed = False

while not command == "END":
    if command == "green":
        for car in range(len(cars)):
            if pass_time - free_window <= 0:
                is_closed = True
                break
            elif pass_time - len(cars[0]) >= 0:
                pass_time -= len(cars[0])
                cars.popleft()
                passed_cars += 1
            else:
                character = pass_time
                is_crashed = True
                print(f"A crash happened!\n{cars[0]} was hit at {cars[0][character]}.")
                break
        pass_time = green_light + free_window
    else:
        cars.append(command)
    if is_crashed:
        break
    if is_closed:
        # break
        pass
    command = input()

if is_crashed is False:
    print(f"Everyone is safe.\n{passed_cars} total cars passed the crossroads.")