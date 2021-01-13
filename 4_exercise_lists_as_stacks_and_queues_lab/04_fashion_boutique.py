from collections import deque

clothes_in_a_box = deque(input().split())
rack_capacity = int(input())
racks = []
current_rack = 0

while clothes_in_a_box:
    if current_rack + int(clothes_in_a_box[-1]) <= rack_capacity:
        current_rack += int(clothes_in_a_box[-1])
        clothes_in_a_box.pop()
    else:
        racks.append(current_rack)
        current_rack = 0

if current_rack > 0:
    racks.append(current_rack)
    current_rack = 0
print(len(racks))
