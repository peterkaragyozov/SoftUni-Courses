from collections import deque

materials_num_stack = [int(x) for x in input().split()]
magic_level_queue = deque([int(x) for x in input().split()])
presents_dict = {}


while True:
    if not materials_num_stack or not magic_level_queue:
        break

    current_material = materials_num_stack[-1]
    current_magic = magic_level_queue[0]

    total_magic = current_material * current_magic
    present = None
    if total_magic in [150, 250, 300, 400]:
        if total_magic == 150:
            present = "Doll"
        elif total_magic == 250:
            present = "Wooden train"
        elif total_magic == 300:
            present = "Teddy bear"
        elif total_magic == 400:
            present = "Bicycle"

        if present:
            if present not in presents_dict:
                presents_dict[present] = 0
            presents_dict[present] += 1

        materials_num_stack.pop()
        magic_level_queue.popleft()
    else:
        if total_magic < 0:
            new_value = current_material + current_magic
            materials_num_stack.pop()
            magic_level_queue.popleft()
            materials_num_stack.append(new_value)
        elif total_magic > 0:
            magic_level_queue.popleft()
            materials_num_stack[-1] += 15

        if current_magic == 0:
            magic_level_queue.popleft()
        if current_material == 0:
            materials_num_stack.pop()

if ("Doll" in presents_dict and "Wooden train" in presents_dict) \
        or ("Teddy bear" in presents_dict and "Bicycle" in presents_dict):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_num_stack:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials_num_stack)])}")
if magic_level_queue:
    print(f"Magic left: {', '.join([str(x) for x in magic_level_queue])}")

presents_dict = dict(sorted(presents_dict.items(), key=lambda x: (x[0], x[1])))
for key, value in presents_dict.items():
    print(f"{key}: {value}")
