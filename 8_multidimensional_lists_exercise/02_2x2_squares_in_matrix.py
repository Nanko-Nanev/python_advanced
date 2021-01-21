(row, col) = [int(x) for x in input().split()]
matrix = []
counter_2x2 = 0

for _ in range(row):
    row_line = input().split()
    matrix.append(row_line)

for i in range(row - 1):
    for j in range(col - 1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            counter_2x2 += 1

print(counter_2x2)