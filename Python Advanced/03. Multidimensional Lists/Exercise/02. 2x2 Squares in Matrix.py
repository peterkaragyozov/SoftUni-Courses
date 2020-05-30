row_count, col_count = [int(x) for x in input().split()]
matrix = []

for _ in range(row_count):
    matrix.append([x for x in input().split()])

count = 0
for row in range(row_count - 1):
    for col in range(col_count - 1):
        if matrix[row][col] == matrix[row+1][col] == matrix[row][col+1] == matrix[row+1][col+1]:
            count += 1
print(count)