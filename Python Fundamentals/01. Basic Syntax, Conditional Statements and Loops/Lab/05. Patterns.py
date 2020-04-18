num = int(input())
for row in range(1, num + 1):
    for col in range(0, row):
        print("*", end="")
    print()

for row in range(num - 1, - 1, - 1):
    for col in range(row - 1, - 1, - 1):
        print("*", end="")
    print()