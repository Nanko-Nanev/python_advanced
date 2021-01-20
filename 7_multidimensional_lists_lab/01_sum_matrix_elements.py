(rows, columns) = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

sum_of_the_matrix = 0

for row in matrix:
    sum_of_the_matrix += sum(row)

print(sum_of_the_matrix)
print(matrix)