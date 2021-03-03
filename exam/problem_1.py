from collections import deque

palm = 0
window = 0
cross = 0

firework = deque([int(el) for el in input().split(", ")])
ex_power = deque([int(el) for el in input().split(", ") if int(el) > 0])


while min(len(firework), len(ex_power)):
    current_firework = firework.popleft()
    current_ex_power = ex_power.pop()
    current_sum = current_firework + current_ex_power

    if current_sum % 3 == 0 and current_sum % 5 != 0:
        palm += 1
    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        window += 1
    elif current_sum % 5 == 0 and current_sum % 3 == 0:
        cross += 1
    else:
        current_firework -= 1
        firework.append(current_firework)
        ex_power.append(current_ex_power)

if palm >= 3 and window >= 3 and cross >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")

if firework:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework])}")

if ex_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in ex_power])}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {window}")
print(f"Crossette Fireworks: {cross}")