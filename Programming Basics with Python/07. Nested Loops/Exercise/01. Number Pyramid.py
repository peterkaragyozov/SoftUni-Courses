number = int(input())
current = 0
line = ""
isBiggerThanN = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        current += 1
        if current > number:
            isBiggerThanN = True
            break
        if col == row:
            print(str(current), end='')
        else:
            print(str(current) + " ", end='')
    if isBiggerThanN:
        break
    print()