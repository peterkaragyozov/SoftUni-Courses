rooms_num = int(input())
empty_chairs = 0
not_enough_chairs_in_room = False

for i in range(1, rooms_num + 1):
    info = input().split(" ")
    chairs = len(info[0])
    people = int(info[1])
    if people > chairs:
        print(f"{people - chairs} more chairs needed in room {i}")
        not_enough_chairs_in_room = True
    else:
        empty_chairs += chairs - people

if empty_chairs >= 0 and not not_enough_chairs_in_room:
    print(f"Game On, {empty_chairs} free chairs left")