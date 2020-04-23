tasks = [int(time) for time in input().split(" ")]


while True:
    line = input().split(" ")
    if line[0] == "End":
        break
    command = line[0]
    if command == "Complete":
        index = int(line[1])
        if 0 <= index < len(tasks):
            tasks[index] = 0
    elif command == "Change":
        index = int(line[1])
        time = int(line[2])
        if 0 <= index < len(tasks):
            tasks[index] = time
    elif command == "Drop":
        index = int(line[1])
        if 0 <= index < len(tasks):
            tasks[index] = -1
    elif line[1] == "Completed":
        counter = 0
        for comp in range(len(tasks)):
            if tasks[comp] == 0:
                counter += 1
        print(counter)
    elif line[1] == "Incomplete":
        counter = 0
        for comp in range(len(tasks)):
            if tasks[comp] > 0:
                counter += 1
        print(counter)
    elif line[1] == "Dropped":
        counter = 0
        for comp in range(len(tasks)):
            if tasks[comp] < 0:
                counter += 1
        print(counter)

incomplete_tasks = [str(time) for time in tasks if time > 0]
print(" ".join(incomplete_tasks))