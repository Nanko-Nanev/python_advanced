from collections import deque

palm = 0
window = 0
cross = 0
perfect_fw = False

firework = deque([int(el) for el in input().split(", ")])
ex_power = [int(el) for el in input().split(", ") if int(el) > 0]

while min(len(firework), len(ex_power)):
    if firework[0] >= 0 and ex_power[-1] >= 0:
        current_value = firework[0] + ex_power[-1]

    else:
        if ex_power[-1] <=0:
            ex_power.pop()
        else:
            firework.pop()
        continue
    if firework[0] <= 0 and ex_power[-1] <= 0:
        firework.popleft()
        ex_power.pop()

    if current_value % 3 == 0 and current_value % 5 == 0:
        cross += 1
        firework.popleft()
        ex_power.pop()

    elif current_value % 3 == 0:
        palm += 1
        firework.popleft()
        ex_power.pop()
    elif current_value % 5 == 0:
        window += 1
        firework.popleft()
        ex_power.pop()
    else:
        firework[0] -= 1
        element = firework.popleft()
        firework.append(element)

    if cross >= 3 and palm >= 3 and window >= 3:
        perfect_fw = True
        break
if perfect_fw:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if len(firework) > 0:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework])}")
if len(ex_power) > 0:
    print(f"Explosive Power left: {', '.join([str(el) for el in ex_power])}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {window}")
print(f"Crossette Fireworks: {cross}")