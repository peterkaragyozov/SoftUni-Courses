owned_tanks = input().split(", ")
commands_num = int(input())

# for tank in owned_tanks:
#     kdskdk

for i in range(commands_num):
    token = input().split(", ")
    command = token[0]
    tank = token[1]
    if command == "Add":
        if tank in owned_tanks:
            print("Tank is already bought")
        else:
            print("Tank successfully bought")
            owned_tanks.append(tank)
    elif command == "Remove":
        if tank in owned_tanks:
            print("Tank successfully sold")
            owned_tanks.remove(tank)
        else:
            print("Tank not found")
    elif command == "Remove At":
        index = int(token[1])
        if index <= len(owned_tanks):
            del owned_tanks[index]
            print(f"Tank successfully sold")
        else:
            print("Index out of range")
    elif command == "Insert":
        index = int(token[1])
        tank = token[2]
        if index > len(owned_tanks):
            print("Index out of range")
        else:
            if tank not in owned_tanks:
                owned_tanks.insert(index, tank)
                print("Tank successfully bought")
            elif tank in owned_tanks:
                print("Tank is already bought")
final_list = ", ".join(owned_tanks)
print(final_list)