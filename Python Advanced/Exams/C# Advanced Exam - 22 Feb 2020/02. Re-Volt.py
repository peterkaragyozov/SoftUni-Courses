def ensure_indexes_in_matrix(n_row, n_col, size):
    if n_row < 0:
        n_row = size - 1
    if n_row >= size:
        n_row = 0

    if n_col < 0:
        n_col = size - 1
    if n_col >= size:
        n_col = 0

    return n_row, n_col


matrix_size = int(input())
commands_count = int(input())

dirs = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

matrix = []
starting_pos = []
player_won = False

for row in range(matrix_size):
    line = list(input())
    if "f" in line:
        starting_pos = [row, line.index("f")]
    matrix.append(line)

current_pos = starting_pos

for i in range(commands_count):
    cmd = input()
    next_row = current_pos[0] + dirs[cmd][0]
    next_col = current_pos[1] + dirs[cmd][1]
    (next_row, next_col) = ensure_indexes_in_matrix(next_row, next_col, matrix_size)

    if matrix[next_row][next_col] == "F":
        matrix[current_pos[0]][current_pos[1]] = "-"
        matrix[next_row][next_col] = "f"
        player_won = True
        break

    elif matrix[next_row][next_col] == "B":
        matrix[current_pos[0]][current_pos[1]] = "-"
        next_row += dirs[cmd][0]
        next_col += dirs[cmd][1]
        (next_row, next_col) = ensure_indexes_in_matrix(next_row, next_col, matrix_size)
        matrix[next_row][next_col] = "f"

    elif matrix[next_row][next_col] == "T":
        next_row -= dirs[cmd][0]
        next_col -= dirs[cmd][1]
        (next_row, next_col) = ensure_indexes_in_matrix(next_row, next_col, matrix_size)

    elif matrix[next_row][next_col] == "-":
        matrix[current_pos[0]][current_pos[1]] = "-"
        matrix[next_row][next_col] = "f"

    current_pos = [next_row, next_col]

if player_won:
    print("Player won!")
else:
    print("Player lost!")

[print(''.join(line)) for line in matrix]