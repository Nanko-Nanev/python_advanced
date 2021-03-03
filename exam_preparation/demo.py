def get_bunnies(mat):
    bunnies = []
    for ro in range(n):
        for co in range(m):
            if mat[ro][co] == "B":
                bunnies.append((ro, co))
    return bunnies


def find_start(mat):
    for _row in range(n):
        for _col in range(m):
            if mat[_row][_col] == "P":
                start = (_row, _col)
    return start


n, m = [int(el) for el in input().split()]

matrix = []
for _ in range(n):
    row = list(input())
    matrix.append(row)

start_row, start_col = find_start(matrix)
row, col = start_row, start_col
commands = list(input())
is_won = False
is_lost = False

for command in commands:
    if command == "L" and col > 0:
        if matrix[row][col - 1] == "B":
            row, col = row, col - 1
            is_lost = True
        else:
            matrix[row][col] = "."
            matrix[row][col - 1] = "P"
            row, col = row, col - 1
    elif command == "L":
        matrix[row][col] = "."
        is_won = True

    if command == "R" and col < n - 1:
        if matrix[row][col + 1] == "B":
            row, col = row, col + 1
            is_lost = True
        else:
            matrix[row][col] = "."
            matrix[row][col + 1] = "P"
            row, col = row, col + 1
    elif command == "R":
        matrix[row][col] = "."
        is_won = True

    if command == "U" and row > 0:
        if matrix[row - 1][col] == "B":
            row, col = row - 1, col
            is_lost = True
        else:
            matrix[row][col] = "."
            matrix[row - 1][col] = "P"
            row, col = row - 1, col
    elif command == "U":
        matrix[row][col] = "."
        is_won = True

    if command == "D" and row < n - 1:
        if matrix[row + 1][col] == "B":
            row, col = row + 1, col
            is_lost = True
        else:
            matrix[row][col] = "."
            matrix[row + 1][col] = "P"
            row, col = row + 1, col
    elif command == "D":
        matrix[row][col] = "."
        is_won = True

    bunnies_coordinates = get_bunnies(matrix)
    for coordinate in bunnies_coordinates:
        r = coordinate[0]
        c = coordinate[1]
        if r + 1 in range(n) and c in range(m):
            if matrix[r + 1][c] == "P":
                is_lost = True
                matrix[r + 1][c] = "B"
            else:
                matrix[r + 1][c] = "B"
        if r - 1 in range(n) and c in range(m):
            if matrix[r - 1][c] == "P":
                is_lost = True
                matrix[r - 1][c] = "B"
            else:
                matrix[r - 1][c] = "B"
        if r in range(n) and c - 1 in range(m):
            if matrix[r][c - 1] == "P":
                is_lost = True
                matrix[r][c - 1] = "B"
            else:
                matrix[r][c - 1] = "B"
        if r in range(n) and c + 1 in range(m):
            if matrix[r][c + 1] == "P":
                is_lost = True
                matrix[r][c + 1] = "B"
            else:
                matrix[r][c + 1] = "B"

    if is_won:
        break

    if is_lost:
        break

for row_ in range(n):
    print(''.join(matrix[row_]))

if is_won:
    print(f"won: {row} {col}")
else:
    print(f"dead: {row} {col}")
