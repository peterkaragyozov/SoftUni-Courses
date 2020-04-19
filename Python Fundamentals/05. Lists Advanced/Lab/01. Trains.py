wagons_n = int(input())

train = [0] * wagons_n

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split(" ")
    instructuons = tokens[0]
    if instructuons == "add":
        count = int(tokens[1])
        train[-1] += count
    elif instructuons == "insert":
        index = int(tokens[1])
        count = int(tokens[2])
        train[index] += count
    elif instructuons == "leave":
        index = int(tokens[1])
        count = int(tokens[2])
        train[index] -= count

print(train)