n = int(input())

dirs = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

matrix = []
snake_pos = []
burrow_one = []
burrow_two = []
food_eaten = 0

for row in range(n):
    line = list(input())
    if "S" in line:
        snake_pos = [row, line.index("S")]
    matrix.append(line)


while True:
    cmd = input()
    direction_change = dirs[cmd]
    next_row = snake_pos[0] + direction_change[0]
    next_col = snake_pos[1] + direction_change[1]
    next_pos = [next_row, next_col]

    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col] == "-":
            matrix[snake_pos[0]][snake_pos[1]] = "."
            matrix[next_row][next_col] = "S"
            snake_pos = next_pos
        elif matrix[next_row][next_col] == "*":
            matrix[snake_pos[0]][snake_pos[1]] = "."
            matrix[next_row][next_col] = "S"
            food_eaten += 1
            snake_pos = next_pos
        elif matrix[next_row][next_col] == "B":
            matrix[snake_pos[0]][snake_pos[1]] = "."
            burrow_one = [next_row, next_col]

            for row in range(n):
                for col in range(n):
                    if matrix[row][col] == "B" and row != next_row and col != next_col:
                        burrow_two = [row, col]
            matrix[next_row][next_col] = "."
            matrix[burrow_two[0]][burrow_two[1]] = "S"
            snake_pos = burrow_two[0], burrow_two[1]

    else:
        matrix[snake_pos[0]][snake_pos[1]] = "."
        print("Game over!")
        break

    if food_eaten == 10:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food_eaten}")
[print("".join(row)) for row in matrix]