pirate_ship_status = [int(i) for i in input().split(">")]
warship_status = [int(i) for i in input().split(">")]

max_health = int(input())

stalemate = True

while True:
    line = input().split(" ")
    if line[0] == "Retire":
        break
    command = line[0]
    if command == "Fire":
        index = int(line[1])
        damage = int(line[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    elif command == "Defend":
        index_start = int(line[1])
        index_end = int(line[2])
        damage = int(line[3])
        if 0 <= index_start < len(pirate_ship_status) and 0 <= index_end < len(pirate_ship_status):
            for i in range(index_start, index_end + 1):
                pirate_ship_status[i] -= damage
                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
    elif command == "Repair":
        index = int(line[1])
        health = int(line[2])
        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health:
                pirate_ship_status[index] = max_health
    elif command == "Status":
        count_needing_repair = 0
        for i in range(len(pirate_ship_status)):
            if pirate_ship_status[i] < 20 / 100 * max_health:
                count_needing_repair += 1
        print(f"{count_needing_repair} sections need repair.")

if stalemate:
    sum_pirate_ship_status = 0
    sum_warship_status = 0
    for i in range(len(pirate_ship_status)):
        sum_pirate_ship_status += pirate_ship_status[i]

    for i in range(len(warship_status)):
        sum_warship_status += warship_status[i]

    print(f"Pirate ship status: {sum_pirate_ship_status}")
    print(f"Warship status: {sum_warship_status}")