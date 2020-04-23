frog_list = input().split(" ")

while True:
    line = input().split(" ")
    command = line[0]
    if command == "Join":
        name = line[1]
        frog_list.append(name)
    elif command == "Jump":
        name = line[1]
        index = int(line[2])
        if 0 <= index < len(frog_list):
            frog_list.insert(index, name)
    elif command == "Dive":
        index = int(line[1])
        if 0 <= index < len(frog_list):
            frog_list.remove(frog_list[index])
    elif command == "First" or command == "Last":
        count = int(line[1])
        if command == "First":
            if count > len(frog_list):
                print(' '.join(frog_list))
            else:
                print(' '.join(frog_list[:count]))
        elif command == "Last":
            if count > len(frog_list):
                print(' '.join(frog_list))
            else:
                print(' '.join(frog_list[len(frog_list) - count:]))
    elif command == "Print":
        if line[1] == "Normal":
            print(f"Frogs: {' '.join(frog_list)}")
        elif line[1] == "Reversed":
            frog_list.reverse()
            print(f"Frogs: {' '.join(frog_list)}")
        break