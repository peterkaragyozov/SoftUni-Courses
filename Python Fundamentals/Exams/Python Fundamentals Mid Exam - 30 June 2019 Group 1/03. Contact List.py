starting_list = input().split(" ")

while True:
    commands = input().split(" ")
    cmd = commands[0]

    if cmd == "Print":
        type = commands[1]

        if type == "Normal":
            starting_list = " ".join(starting_list)
        elif type == "Reversed":
            starting_list = " ".join(reversed(starting_list))
        print(f"Contacts: {starting_list}")
        break

    elif cmd == "Add":
        contact = commands[1]
        index = int(commands[2])
        if contact not in starting_list:
            starting_list.append(contact)
        elif (contact in starting_list) and (0 <= index < len(starting_list)):
            starting_list.insert(index, contact)

    elif cmd == "Remove":
        index = int(commands[1])
        if 0 <= index < len(starting_list):
            del starting_list[index]

    elif cmd == "Export":
        start = int(commands[1])
        count = int(commands[2])
        print(" ".join(starting_list[start:start + count:]))