guests = {}
unliked_meals_count = 0
while True:
    line = input()
    if line == "Stop":
        guests = dict(sorted(guests.items(), key=lambda x: (-len(x[1]), x[0])))
        for k, v in guests.items():
            print(f"{k}: {', '.join(v)}")
        print(f"Unliked meals: {unliked_meals_count}")
        break
    line = line.split("-")
    cmd = line[0]
    guest = line[1]
    meal = line[2]
    if cmd == "Like":
        if guest in guests:
            if meal in guests[guest]:
                continue
            guests[guest].append(meal)
        else:
            guests[guest] = []
            guests[guest].append(meal)
    elif cmd == "Unlike":
        if guest in guests:
            if meal in guests[guest]:
                guests[guest].remove(meal)
                unliked_meals_count += 1
                print(f"{guest} doesn't like the {meal}.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")