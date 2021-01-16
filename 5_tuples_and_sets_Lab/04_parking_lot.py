n = int(input())
cars_in = set([])

for _ in range(n):
    command, plate = input().split(", ")

    if command == "IN":
        cars_in.add(plate)
    else:
        cars_in.remove(plate)

if cars_in:
    for car in cars_in:
        print(car)
else:
    print("Parking Lot is Empty")