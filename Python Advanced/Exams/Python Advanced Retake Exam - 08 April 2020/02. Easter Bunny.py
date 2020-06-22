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