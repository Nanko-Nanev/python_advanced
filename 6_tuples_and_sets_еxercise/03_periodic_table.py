n = int(input())
unique_chemical = set([])

for _ in range(n):
    command = input().split()
    for el in command:
        unique_chemical.add(el)

for chemical in unique_chemical:
    print(chemical)