energy = 100
coins = 100

events = input().split("|")

for event in events:
    args = event.split("-")
    name = args[0]
    number = int(args[1])

    if name == "rest":
        temp = 0
        if energy + number <= 100:
            energy += number
            temp = number
        else:
            temp = 100 - energy
            energy = 100

        print(f"You gained {temp} energy.")
        print(f"Current energy: {energy}.")
    elif name == "order":
        if energy - 30 >= 0:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins - number > 0:
            coins -= number
            print(f"You bought {name}.")
        else:
            print(f"Closed! Cannot afford {name}.")
            break

if coins - number > 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")