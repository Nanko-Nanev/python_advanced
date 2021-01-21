from collections import deque

(row, col) = [int(x) for x in input().split()]
string_input = input()
string = deque("")
matrix = []

for _ in range(row):
    matrix.append([0] * col)

while len(string) <= (row * col):
    string += string_input

for r in range(row):
    for c in range(col):
        matrix[r][c] = string[0]
        string.popleft()

for current_row in range(len(matrix)):
    if current_row % 2 == 1:
        matrix[current_row].reverse()
    else:
        pass

for current_row in range(len(matrix)):
    print("".join(matrix[current_row]))