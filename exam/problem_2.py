def valid_position(row, col, matrix):
    if 0 <= row <= len(matrix) and 0 <= col <= len(matrix[0]):
        return True
    else:
        return False


n = int(input())
board = []
player_position = []
coins = 0
dead = 1
path = []

for i in range(n):
    board.append([el for el in input().split()])

for row in range(n):
    for col in range(n):
        if board[row][col] == "P":
            player_position = [row, col]


(p_row, p_col) = player_position

command = input()
while True:
    board[p_row][p_col] = 0
    if command == "up":
        p_row -= 1
    elif command == "down":
        p_row += 1
    elif command == "left":
        p_col -= 1
    elif command == "right":
        p_col += 1
    else:
        command = input()
        continue

    if valid_position(p_row, p_col, board):
        if board[p_row][p_col] == "X":
            dead = 0
            break
        elif str(board[p_row][p_col]).isdigit():
            coins += int(board[p_row][p_col])
            path.append([p_row, p_col])
            if coins >= 100:
                break
    else:
        dead = 0
        break
    command = input()

if dead == 0:
    coins = round(coins / 2)
    print(f"Game over! You've collected {coins} coins.")
else:
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")

print("Your path:")
for p in path:
    print(p)