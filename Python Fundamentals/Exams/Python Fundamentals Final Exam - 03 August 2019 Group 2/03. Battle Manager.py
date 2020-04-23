battles_dict = {}

while True:
    line = input()
    if line == "Results":
        print(f"People count: {len(battles_dict)}")
        battles_dict = dict(sorted(battles_dict.items(), key=lambda x: (-(x[1][0]), x[0])))

        for k, v in battles_dict.items():
            v = [str(x) for x in v]
            print(f"{k} - {' - '.join(v)}")
        break

    line = line.split(":")
    cmd = line[0]

    if cmd == "Add":
        name = line[1]
        health = int(line[2])
        energy = int(line[3])
        if name not in battles_dict:
            battles_dict[name] = [0] * 2
        battles_dict[name][0] += health
        battles_dict[name][1] += energy

    elif cmd == "Attack":
        attacker = line[1]
        defender = line[2]
        damage = int(line[3])
        if (attacker in battles_dict) and (defender in battles_dict):
            battles_dict[defender][0] -= damage
            if battles_dict[defender][0] <= 0:
                print(f"{defender} was disqualified!")
                del battles_dict[defender]
            battles_dict[attacker][1] -= 1
            if battles_dict[attacker][1] == 0:
                print(f"{attacker} was disqualified!")
                del battles_dict[attacker]

    elif cmd == "Delete":
        name = line[1]
        if name in battles_dict:
            del battles_dict[name]
        if name == "All":
            battles_dict = {}