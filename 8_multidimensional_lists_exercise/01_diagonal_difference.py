n = int(input())

matrix = []
sum_of_primary_diagonal = 0
sum_of_secondary_diagonal = 0
col_index = n - 1

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for row in range(n):
    sum_of_primary_diagonal += matrix[row][row]
    sum_of_secondary_diagonal += matrix[row][col_index]
    col_index -= 1

dif = abs( sum_of_primary_diagonal - sum_of_secondary_diagonal)

print(dif)