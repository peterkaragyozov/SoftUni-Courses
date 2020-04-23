heroes = {}

while True:
    line = input()
    if line == "End":
        sorted_heroes = sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0]))
        print("Heroes:")
        for i in sorted_heroes:
            print(f"== {i[0]}: {', '.join(i[1])}")
        break
    line = line.split(" ")
    cmd = line[0]
    hero = line[1]
    if cmd == "Enroll":
        if hero in heroes:
            print(f"{hero} is already enrolled.")
            continue
        heroes[hero] = []
    elif cmd == "Learn":
        spell = line[2]
        if hero in heroes:
            if spell in heroes[hero]:
                print(f"{hero} has already learnt {spell}.")
                continue
            else:
                heroes[hero].append(spell)
                continue
        print(f"{hero} doesn't exist.")
    elif cmd == "Unlearn":
        spell = line[2]
        if hero in heroes:
            if spell in heroes[hero]:
                heroes[hero].remove(spell)
                continue
            else:
                print(f"{hero} doesn't know {spell}.")
                continue
        print(f"{hero} doesn't exist.")