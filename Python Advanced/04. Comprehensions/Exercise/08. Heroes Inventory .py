heroes = {name: {} for name in input().split(", ")}

while True:
    line = input().split("-")
    name = line[0]
    if name == "End":
        break

    item = line[1]
    cost = int(line[2])

    if item not in heroes[name]:
        heroes[name][item] = cost

[print(f"{name} -> Items: {len(heroes[name])}, Cost: {sum(heroes[name].values())}") for name in heroes]