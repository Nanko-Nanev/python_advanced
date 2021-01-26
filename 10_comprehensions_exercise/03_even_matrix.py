n = int(input())
matrix = []
for _ in range(n):
    row = [int(ch) for ch in input().split(", ") if int(ch) % 2 == 0]
    matrix.append(row)
print(matrix)

