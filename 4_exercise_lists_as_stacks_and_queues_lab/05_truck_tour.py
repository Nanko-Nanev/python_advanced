n = int(input())
petrol = []
dist = []
tank = 0
current_index = 0

for i in range(n):
    add_petrol, add_distance = input().split()
    petrol.append(add_petrol)
    dist.append(add_distance)

petrol.append(petrol[0])
dist.append(dist[0])

for i in range(len(petrol)):
    add_to_tank = int(petrol[i]) - int(dist[i])
    if tank + add_to_tank < 0:
        current_index += 1
        tank = 0
        petrol.append(petrol[current_index])
        dist.append(dist[current_index])
        continue
    else:
        tank += add_to_tank

print(current_index)