phonebook = {}

while True:
    line = input().split("-")
    if len(line) == 1:
        break
    name = line[0]
    number = line[1]
    phonebook[name] = number

n = int(line[0])

for _ in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")