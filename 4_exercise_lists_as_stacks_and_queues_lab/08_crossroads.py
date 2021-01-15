from collections import deque

green_light = int(input())
free_window = int(input())

crossroads = deque([])
on_traffic = deque([])

command = input()

while not command == "END":
    if command == "green":
        # start the green cycle
        green = green_light
        while green > 0:
            if on_traffic:
                current_car = on_traffic.popleft()
                if len(current_car) >= green_light:
                    green -= len(current_car)
                    crossroads.append(current_car)
                    if green > 0:
                        crossroads.popleft()
                else:
                    pass
    else:
        on_traffic.append(command)

    command = input()