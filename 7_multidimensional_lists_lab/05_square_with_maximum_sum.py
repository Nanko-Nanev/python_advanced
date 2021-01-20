(rows, columns) = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    row = [str(x) for x in input().split(", ")]
    matrix.append(row)

max_sum = -99999999999
index_of_max_sum = []

for i in range(rows - 1):
    for j in range(columns - 1):
        current_sum = int(matrix[i][j]) + int(matrix[i][j+1]) + int(matrix[i+1][j]) + int(matrix[i+1][j+1])
        if max_sum < current_sum:
            max_sum = current_sum
            index_of_max_sum = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]

print(index_of_max_sum[0], index_of_max_sum[1])
print(index_of_max_sum[2], index_of_max_sum[3])
print(max_sum)