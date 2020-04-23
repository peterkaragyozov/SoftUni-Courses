initial_list = input().split("!")

while True:
    line = input().split(" ")
    if line[1] == "Shopping!":
        break
    command = line[0]
    if command == "Urgent":
        item = line[1]
        if item not in initial_list:
            initial_list.insert(0, item)
    elif command == "Unnecessary":
        item = line[1]
        if item in initial_list:
            initial_list.remove(item)
    elif command == "Correct":
        item = line[1]
        new_item = line[2]
        if item in initial_list:
            ind = initial_list.index(item)
            initial_list[ind] = new_item
    elif command == "Rearrange":
        item = line[1]
        if item in initial_list:
            ind = initial_list.index(item)
            initial_list.append(initial_list.pop(ind))
print(", ".join(initial_list))