n = int(input())
max_hp = 100
max_mp = 200

heroes_dict = {}

for i in range(n):
    line = input().split(" ")
    hero = line[0]
    hp = int(line[1])
    mp = int(line[2])

    heroes_dict[hero] = [0] * 2
    heroes_dict[hero][0] = hp
    heroes_dict[hero][1] = mp

while True:
    line = input()
    if line == "End":
        heroes_dict = dict(sorted(heroes_dict.items(), key=lambda x: (-x[1][0], x[0])))

        for k, v in heroes_dict.items():
            print(f"{k}\nHP: {v[0]}\nMP: {v[1]}")
        break

    line = line.split(" - ")
    cmd = line[0]
    hero = line[1]

    if cmd == "CastSpell":
        needed_mp = int(line[2])
        spell_name = line[3]

        if heroes_dict[hero][1] >= needed_mp:
            heroes_dict[hero][1] -= needed_mp
            print(f"{hero} has successfully cast {spell_name} and now has {heroes_dict[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif cmd == "TakeDamage":
        damage = int(line[2])
        attacker = line[3]

        heroes_dict[hero][0] -= damage
        if heroes_dict[hero][0] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero][0]} HP left!")
        else:
            del heroes_dict[hero]
            print(f"{hero} has been killed by {attacker}!")

    elif cmd == "Recharge":
        amount = int(line[2])
        if heroes_dict[hero][1] + amount > max_mp:
            amount = max_mp - heroes_dict[hero][1]
            heroes_dict[hero][1] = max_mp
        else:
            heroes_dict[hero][1] += amount
        print(f"{hero} recharged for {amount} MP!")

    elif cmd == "Heal":
        amount = int(line[2])
        if heroes_dict[hero][0] + amount > max_hp:
            amount = max_hp - heroes_dict[hero][0]
            heroes_dict[hero][0] = max_hp
        else:
            heroes_dict[hero][0] += amount
        print(f"{hero} healed for {amount} HP!")