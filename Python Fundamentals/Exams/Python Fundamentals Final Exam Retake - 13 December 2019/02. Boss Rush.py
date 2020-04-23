import re

n = int(input())
pattern = r"\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#"
for _ in range(n):
    line = input()
    match = re.match(pattern, line)
    if match is None:
        print("Access denied!")
    else:
        name = match[1]
        title = match[2]
        strength = len(name)
        armour = len(title)
        print(f"{name}, The {title}\n>> Strength: {strength}\n>> Armour: {armour}")