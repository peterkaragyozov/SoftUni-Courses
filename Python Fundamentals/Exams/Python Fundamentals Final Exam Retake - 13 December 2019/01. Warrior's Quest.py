skill = input()

while True:
    line = input()
    if line == "For Azeroth":
        break
    line = line.split(" ")
    cmd = line[0]
    if cmd == "GladiatorStance":
        skill = skill.upper()
        print(skill)
    elif cmd == "DefensiveStance":
        skill = skill.lower()
        print(skill)
    elif cmd == "Dispel":
        idx = int(line[1])
        letter = line[2]

        if idx < len(skill):
            skill = list(skill)
            skill[idx] = letter
            skill = "".join(skill)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif cmd == "Target":
        substring = line[2]
        if line[1] == "Change":
            second_substring = line[3]
            skill = skill.replace(substring, second_substring)
            print(skill)
        elif line[1] == "Remove":
            skill = skill.replace(substring, "")
            print(skill)
        else:
            print("Command doesn't exist!")
    else:
        print("Command doesn't exist!")