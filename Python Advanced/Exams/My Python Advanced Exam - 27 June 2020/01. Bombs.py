from collections import deque

bomb_effects_queue = deque(int(x) for x in input().split(", "))
bomb_casings_stack = [int(x) for x in input().split(", ")]

bombs_pouch_dict = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
bomb_types = ["Datura Bombs", "Cherry Bombs", "Smoke Decoy Bombs"]
check = False

while bomb_effects_queue and bomb_casings_stack:
    current_effect = bomb_effects_queue[0]
    current_casing = bomb_casings_stack[-1]

    total_elements = current_effect + current_casing
    bomb = ''

    if total_elements == 40:
        bomb = "Datura Bombs"
        bomb_effects_queue.popleft()
        bomb_casings_stack.pop()

    elif total_elements == 60:
        bomb = "Cherry Bombs"
        bomb_effects_queue.popleft()
        bomb_casings_stack.pop()

    elif total_elements == 120:
        bomb = "Smoke Decoy Bombs"
        bomb_effects_queue.popleft()
        bomb_casings_stack.pop()

    else:
        bomb_casings_stack[-1] -= 5

    if bomb:
        bombs_pouch_dict[bomb] += 1

    if (bomb_types[0] in bombs_pouch_dict) and (bomb_types[1] in bombs_pouch_dict) and (bomb_types[2] in bombs_pouch_dict):
        if bombs_pouch_dict[bomb_types[0]] >= 3 and bombs_pouch_dict[bomb_types[1]] >= 3 and bombs_pouch_dict[bomb_types[2]] >= 3:
            check = True
            break



if (bomb_types[0] in bombs_pouch_dict) and (bomb_types[1] in bombs_pouch_dict) and (bomb_types[2] in bombs_pouch_dict):
    if bombs_pouch_dict[bomb_types[0]] >= 3 and bombs_pouch_dict[bomb_types[1]] >= 3 and bombs_pouch_dict[bomb_types[2]] >= 3:
        check = True

if check:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects_queue:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects_queue])}")
else:
    print("Bomb Effects: empty")

if bomb_casings_stack:
    print(f"Bomb Casings: {', '.join([str(x) for x in reversed(bomb_casings_stack)])}")
else:
    print("Bomb Casings: empty")

bombs_pouch_dict = dict(sorted(bombs_pouch_dict.items(), key=lambda x: x[0]))
for key, value in bombs_pouch_dict.items():
    print(f"{key}: {value}")