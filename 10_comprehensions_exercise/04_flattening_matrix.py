n = int(input())
matrix = []

# for _ in range(n):
#     row = [int(ch) for ch in input().split(", ")]
#     matrix.append(row)
#
# print(matrix)

for _ in range(n):
    matrix += [int(ch) for ch in input().split(", ")]

print(matrix)

