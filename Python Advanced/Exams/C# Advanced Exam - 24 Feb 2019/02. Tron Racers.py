def ensure_indexes_in_matrix(next_row, next_col, matrix_size):
    if next_row < 0:
        next_row = matrix_size - 1
    if next_row >= matrix_size:
        next_row = 0

    if next_col < 0:
        next_col = matrix_size - 1
    if next_col >= matrix_size:
        next_col = 0

    return (next_row, next_col)


matrix_size = int(input())

dirs = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

matrix = []
first_player_pos = []
second_player_pos = []

for row in range(matrix_size):
    line = list(input())
    if "f" in line:
        first_player_pos = [row, line.index("f")]
    if "s" in line:
        second_player_pos = [row, line.index("s")]
    matrix.append(line)

first_current_pos = first_player_pos
second_current_pos = second_player_pos

while True:
    commands_line = input().split()
    cmd_first = commands_line[0]
    cmd_second = commands_line[1]

    next_row_f = first_current_pos[0] + dirs[cmd_first][0]
    next_col_f = first_current_pos[1] + dirs[cmd_first][1]

    next_row_s = second_current_pos[0] + dirs[cmd_second][0]
    next_col_s = second_current_pos[1] + dirs[cmd_second][1]

    (next_row_f, next_col_f) = ensure_indexes_in_matrix(next_row_f, next_col_f, matrix_size)
    (next_row_s, next_col_s) = ensure_indexes_in_matrix(next_row_s, next_col_s, matrix_size)

    if matrix[next_row_f][next_col_f] == "s":
        matrix[next_row_f][next_col_f] = "x"
        break
    else:
        matrix[next_row_f][next_col_f] = "f"
    first_current_pos = [next_row_f, next_col_f]

    if matrix[next_row_s][next_col_s] == "f":
        matrix[next_row_s][next_col_s] = "x"
        break
    else:
        matrix[next_row_s][next_col_s] = "s"
    second_current_pos = [next_row_s, next_col_s]

[print(''.join(line)) for line in matrix]