(row, col) = [int(x) for x in input().split()]
matrix = []
END_CMD = "END"
SWAP_CMD = "swap"

for _ in range(row):
    current_row = input().split()
    matrix.append(current_row)

cmd = input()
while not cmd == END_CMD:
    command = cmd.split()
    if command[0] == SWAP_CMD and len(command) == 5:  # and command[1:4].isdigit():
        a_r = int(command[1])
        a_c = int(command[2])
        b_r = int(command[3])
        b_c = int(command[4])
        if 0 <= a_r <= row and 0 <= a_c <= col and 0 <= b_r <= row and 0 <= b_c <= col:
            matrix[a_r][a_c], matrix[b_r][b_c] = matrix[b_r][b_c], matrix[a_r][a_c]
            for row_i in range(row):
                print(" ".join(matrix[row_i]))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    cmd = input()