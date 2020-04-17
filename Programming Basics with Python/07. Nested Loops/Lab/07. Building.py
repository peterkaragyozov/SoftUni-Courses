number_floors = int(input())
number_rooms = int(input())


for floor in range(number_floors, 0, -1):
    apartments_on_floor = ""
    for room in range(number_rooms):
        if floor == number_floors:

            apartments_on_floor += f"L{floor}{room} "
            continue
        if floor % 2 == 0:
            apartments_on_floor += f"O{floor}{room} "
        else:
            apartments_on_floor += f"A{floor}{room} "

    print(apartments_on_floor.strip())