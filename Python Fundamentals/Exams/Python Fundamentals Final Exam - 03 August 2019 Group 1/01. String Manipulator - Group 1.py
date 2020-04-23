string = input()

while True:
    line = input()
    if line == "End":
        break
    line = line.split(" ")
    cmd = line[0]
    if cmd == "Translate":
        character = line[1]
        replacement = line[2]
        new_string = ""
        for i in string:
            if i == character:
                new_string += replacement
            else:
                new_string += i
        string = new_string
        print(string)
    elif cmd == "Includes":
        check = line[1]
        if check in string:
            print("True")
        else:
            print("False")
    elif cmd == "Start":
        checking = line[1]
        if string[:len(checking)] == checking:
            print("True")
        else:
            print("False")
    elif cmd == "Lowercase":
        string = string.lower()
        print(string)
    elif cmd == "FindIndex":
        character = line[1]
        last_index = string.rfind(character)
        print(last_index)
    elif cmd == "Remove":
        start = int(line[1])
        count = int(line[2])
        remaining_characters = string[start+count:]
        string = string[:start] + remaining_characters
        print(string)