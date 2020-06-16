presents_count = int(input())
neighbourhood_size = int(input())

dirs = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

neighbourhood = []
santa_position = []
nice_kids_counter = 0

for row in range(neighbourhood_size):
    line = list(input().split())
    if "S" in line:
        santa_position = [row, line.index("S")]
    neighbourhood.append(line)

while True:
    command = input()
    if command == "Christmas morning":
        break

    direction_change = dirs[command]
    next_row = santa_position[0] + direction_change[0]
    next_col = santa_position[1] + direction_change[1]
    next_pos = [next_row, next_col]

    if 0 <= next_row < neighbourhood_size and 0 <= next_col < neighbourhood_size:
        if neighbourhood[next_row][next_col] == "X":
            #naughty kid
            neighbourhood[santa_position[0]][santa_position[1]] = "-"
            neighbourhood[next_row][next_col] = "S"
            santa_position = next_pos
        elif neighbourhood[next_row][next_col] == "V":
            # nice kid
            neighbourhood[santa_position[0]][santa_position[1]] = "-"
            neighbourhood[next_row][next_col] = "S"
            santa_position = next_pos
            presents_count -= 1
            nice_kids_counter += 1
        elif neighbourhood[next_row][next_col] == "C":
            #cookies
            neighbourhood[santa_position[0]][santa_position[1]] = "-"
            neighbourhood[next_row][next_col] = "S"
            santa_position = next_pos
            command = ["up", "down", "right", "left"]
            for com in command:
                direction_change = dirs[com]
                next_row = santa_position[0] + direction_change[0]
                next_col = santa_position[1] + direction_change[1]
                next_pos = [next_row, next_col]
                if neighbourhood[next_row][next_col] == "X":
                    # naughty kid
                    neighbourhood[next_row][next_col] = "-"
                    presents_count -= 1
                elif neighbourhood[next_row][next_col] == "V":
                    # nice kid
                    neighbourhood[next_row][next_col] = "-"
                    presents_count -= 1
                    nice_kids_counter += 1

                if presents_count <= 0 and any("V" in i for i in neighbourhood):
                    print("Santa ran out of presents!")
                    break
            break
        elif neighbourhood[next_row][next_col] == "-":
            neighbourhood[santa_position[0]][santa_position[1]] = "-"
            neighbourhood[next_row][next_col] = "S"
            santa_position = next_pos

    if presents_count == 0 and any("V" in i for i in neighbourhood):
        print("Santa ran out of presents!")
        break

    if not any("V" in i for i in neighbourhood):
        break

[print(" ".join(row)) for row in neighbourhood]

remained_nice_kids = 0
for row in range(neighbourhood_size):
    for col in range(neighbourhood_size):
        if neighbourhood[row][col] == "V":
            remained_nice_kids += 1


if any("V" in i for i in neighbourhood):
    print(f"No presents for {remained_nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_counter} happy nice kid/s.")


# Second Way:
# def drop_presents(pos, matrix, available_presents):
#     row = pos[0]
#     col = pos[1]
#     result = 0
#
#     if matrix[row][col - 1] in "XV" and available_presents > 0:
#         result += 1
#         matrix[row][col - 1] = "-"
#         available_presents -= 1
#
#     if matrix[row][col + 1] in "XV" and available_presents > 0:
#         result += 1
#         matrix[row][col + 1] = "-"
#         available_presents -= 1
#
#     if matrix[row - 1][col] in "XV" and available_presents > 0:
#         result += 1
#         matrix[row - 1][col] = "-"
#         available_presents -= 1
#
#     if matrix[row + 1][col] in "XV" and available_presents > 0:
#         result += 1
#         matrix[row + 1][col] = "-"
#         available_presents -= 1
#
#     return result
#
#
# def get_nice_kids(matrix):
#     result = 0
#     for row in range(len(matrix)):
#         for col in range(len(matrix)):
#             if matrix[row][col] == "V":
#                 result += 1
#     return result
#
#
# presents = int(input())
# n = int(input())
# santa_pos = []
#
# matrix = []
# directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
# total_nice_kids = 0
#
# for row in range(n):
#     line = input().split()
#     for col in range(n):
#         if line[col] == "S":
#             santa_pos = [row, col]
#         if line[col] == "V":
#             total_nice_kids += 1
#     matrix.append(line)
#
# while True:
#     line = input()
#     if line == "Christmas morning":
#         break
#
#     dir_changes = directions[line]
#     new_pos = [santa_pos[0] + dir_changes[0], santa_pos[1] + dir_changes[1]]
#
#     if matrix[new_pos[0]][new_pos[1]] == "V":
#         presents -= 1
#     elif matrix[new_pos[0]][new_pos[1]] == "C":
#         dropped_presents = drop_presents(new_pos, matrix, presents)
#         presents -= dropped_presents
#
#     matrix[santa_pos[0]][santa_pos[1]] = "-"
#     santa_pos = new_pos
#     matrix[santa_pos[0]][santa_pos[1]] = "S"
#
#     if presents <= 0 and get_nice_kids(matrix):
#         print("Santa ran out of presents!")
#         break
#
#     if not get_nice_kids(matrix):
#         break
#
# [print(" ".join(row)) for row in matrix]
# nice_kids = get_nice_kids(matrix)
#
# if nice_kids > 0:
#     print(f"No presents for {nice_kids} nice kid/s.")
# else:
#     print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")