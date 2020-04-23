string = input()

while True:
    line = input()
    if line == "Done":
        break
    line = line.split(" ")
    cmd = line[0]
    if cmd == "Change":
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
    elif cmd == "End":
        checking = line[1]
        if string[-len(checking):] == checking:
            print("True")
        else:
            print("False")
    elif cmd == "Uppercase":
        string = string.upper()
        print(string)
    elif cmd == "FindIndex":
        character = line[1]
        first_index = string.find(character)
        print(first_index)
    elif cmd == "Cut":
        start = int(line[1])
        length = int(line[2])
        string = string[start:start+length]
        print(string)