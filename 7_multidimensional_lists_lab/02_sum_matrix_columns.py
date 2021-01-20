(rows, columns) = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

sums = [0] * columns

for row in range(rows):
    for column in range(columns):
        sums[column] += matrix[row][column]

for summ in sums:
    print(summ)