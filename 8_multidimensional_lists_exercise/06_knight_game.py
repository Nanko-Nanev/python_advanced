n = int(input())
matrix = []
all_killers = {}
KNIGHT = "K"
kills = 0
knights_needed_to_be_removed = 0
move_r = [-2, -2, -1, -1, 1, 1, 2, 2]
move_c = [-1, 1, -2, 2, -2, 2, -1, 1]
possible_moves = len(move_r)
checking = True

for _ in range(n):
    row = input()
    current_row = []
    for ch in row:
        current_row.append(ch)
    matrix.append(current_row)

while checking:
    for row in range(n):
        for col in range(len(matrix[row])):
            if matrix[row][col] == KNIGHT:
                kills = 0
                for i in range(possible_moves):
                    move_row = row + move_r[i]
                    move_col = col + move_c[i]
                    if 0 <= move_row < n and 0 <= move_col < n:
                        if matrix[move_row][move_col] == KNIGHT:
                            kills += 1
                if kills > 0:
                    all_killers[row, col] = kills
    if len(all_killers) > 0:
        top_killer = list(max(all_killers, key=all_killers.get))
        top_r = int(top_killer[0])
        top_c = int(top_killer[1])
        matrix[top_r][top_c] = 0
        del all_killers[top_r, top_c]
        knights_needed_to_be_removed += 1
        all_killers = {}
    else:
        checking = False

print(knights_needed_to_be_removed)