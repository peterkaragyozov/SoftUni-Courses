def calculate_primary_diagonal_sum(matrix):
    primary_diagonal_sum = 0

    for i in range(len(matrix)):
        primary_diagonal_sum += matrix[i][i]
    return primary_diagonal_sum

size = int(input())
matrix = []

for _ in range(size):
    line = [int(x) for x in input().split()]
    matrix.append(line)
print(calculate_primary_diagonal_sum(matrix))