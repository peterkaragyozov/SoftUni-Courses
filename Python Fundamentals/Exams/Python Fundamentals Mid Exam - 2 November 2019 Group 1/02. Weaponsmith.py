parts = input().split("|")

while True:
    line = input()
    if line == "Done":
        print(f"You crafted {''.join(parts)}!")
        break
    line = line.split(" ")
    command = line[1]
    if command == "Left":
        index = int(line[2])
        if 0 < index <= len(parts):
            parts[index - 1], parts[index] = parts[index], parts[index - 1]
        continue
    elif command == "Right":
        index = int(line[2])
        if 0 <= index < len(parts) - 1:
            parts[index], parts[index + 1] = parts[index + 1], parts[index]
        continue
    elif command == "Even":
        elements = []
        for i in range(len(parts)):
            if i % 2 == 0:
                elements.append(parts[i])
        print(" ".join(elements))
    elif command == "Odd":
        elements = []
        for i in range(len(parts)):
            if i % 2 != 0:
                elements.append(parts[i])
        print(" ".join(elements))