from collections import deque

rows_count, columns_count = [int(x) for x in input().split(" ")]
snake = deque(input())

matrix = []

# for _ in range(rows_count):
#     matrix.append([0] * columns_count)

for row in range(rows_count):
    matrix.append([])
    for col in range(columns_count):
        matrix[row].append([])

for row in range(rows_count):
    for col in range(columns_count):
        current_col = col
        current_char = snake.popleft()
        if row % 2 != 0:
            current_col = columns_count - 1 - col
        matrix[row][current_col] = current_char
        snake.append(current_char)

for row in matrix:
    print("".join(row))