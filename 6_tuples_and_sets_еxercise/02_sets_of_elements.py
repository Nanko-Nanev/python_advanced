n, m = input().split()
set_n = set([])
set_m = set([])

for _ in range(int(n)):
    set_n.add(input())

for _ in range(int(m)):
    set_m.add(input())

new_set = set_n.intersection(set_m)

for el in new_set:
    print(el)