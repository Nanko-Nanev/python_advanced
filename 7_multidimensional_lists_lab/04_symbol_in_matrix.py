n = int(input())
matrix = []

for i in range(n):
    row = [str(ch) for ch in input()]
    matrix.append(row)

search = input()
result = ""

for i in range(n):
    for j in range(n):
        if matrix[i][j] == search:
            result = f"({i}, {j})"

if result:
    print(result)
else:
    print(f"{search} does not occur in the matrix")