year = input()

while True:
    year = str(int(year) + 1)
    if len(year) == len(set(year)):
        print(year)
        break