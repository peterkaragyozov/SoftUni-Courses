field_size = int(input())
matrix = []
starting_pos = []

directions = {"left": [0, -1], "right": [0, 1], "up": [-1, 0], "down": [1, 0]}
total_eggs_collected = {"left": 0, "right": 0, "up": 0, "down": 0}
eggs_coordinates = {"left": [], "right": [], "up": [], "down": []}

for i in range(field_size):
    line = input().split()
    if 'B' in line:
        starting_pos = [i, line.index("B")]
    matrix.append(line)

for key in directions:
    if directions[key]:
        bunny_pos = starting_pos

        while True:
            next_pos = [bunny_pos[0] + directions[key][0], bunny_pos[1] + directions[key][1]]
            if 0 <= next_pos[0] < len(matrix) and 0 <= next_pos[1] < len(matrix):
                bunny_pos = next_pos
                if matrix[next_pos[0]][next_pos[1]] == "X":
                    directions[key].clear()
                    break
                else:
                    total_eggs_collected[key] += int(matrix[next_pos[0]][next_pos[1]])
                    eggs_coordinates[key].append(next_pos)
            else:
                directions[key].clear()
                break

for key in eggs_coordinates:
    if not eggs_coordinates[key]:
        del total_eggs_collected[key]

best_direction = max(total_eggs_collected, key=lambda k: total_eggs_collected[k])

print(best_direction)
[print(pos) for pos in eggs_coordinates[best_direction]]
print(total_eggs_collected[best_direction])



# Second Way:

# def is_valid(number, size):
#     return 0 <= number < size
#
#
# n = int(input())
#
# bunny_pos = ()
# best_sum = -999999999999999999999999
# best_dir = ""
# directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
# field = []
#
# for row in range(n):
#     line = input().split()
#     if "B" in line:
#         bunny_pos = (row, line.index("B"))
#     field.append(line)
#
# for direction in directions:
#     current_sum = 0
#     row = bunny_pos[0]
#     col = bunny_pos[1]
#
#     row_changes = directions[direction][0]
#     col_changes = directions[direction][1]
#
#     if not is_valid(row + row_changes, n) or not is_valid(col + col_changes, n):
#         continue
#
#     while is_valid(row, n) and is_valid(col, n):
#         current_cell = field[row][col]
#         if current_cell != "B" and current_cell != "X":
#             current_sum += int(current_cell)
#         elif current_cell == "X":
#             break
#         row += row_changes
#         col += col_changes
#
#     if current_sum > best_sum:
#         best_sum = current_sum
#         best_dir = direction
#
# print(best_dir)
#
# row_changes = directions[best_dir][0]
# col_changes = directions[best_dir][1]
#
# row = bunny_pos[0] + row_changes
# col = bunny_pos[1] + col_changes
#
# while is_valid(row, n) and is_valid(col, n):
#     if field[row][col] == "X":
#         break
#     print([row, col])
#     row += row_changes
#     col += col_changes
#
# print(best_sum)