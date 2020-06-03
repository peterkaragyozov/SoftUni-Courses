row_count, column_count = [int(x) for x in input().split()]

matrix = [[f"{chr(row)}{chr(row + col)}{chr(row)}" for col in range(column_count)] for row in range(97, 97 + row_count)]

[print(' '.join(row)) for row in matrix]