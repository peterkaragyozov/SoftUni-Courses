rows_count, columns_count = [int(x) for x in input().split()]
matrix = []
best_sum = -9999999
best_matrix = []

for _ in range(rows_count):
    line = [int(x) for x in input().split()]
    matrix.append(line)

for row in range(rows_count - 2):
    for col in range(columns_count - 2):
        submatrix = []
        current_sum = 0
        row_counter = 0
        for r in range(row, row + 3):
            submatrix.append([])
            for c in range(col, col + 3):
                submatrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1
        if current_sum > best_sum:
            best_sum = current_sum
            best_matrix = submatrix

print(f"Sum = {best_sum}")
for row in best_matrix:
    print(' '.join([str(x) for x in row]))