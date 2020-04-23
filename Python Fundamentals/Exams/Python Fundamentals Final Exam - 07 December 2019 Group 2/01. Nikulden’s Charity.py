string = input()

while True:
    line = input()
    if line == "Finish":
        break
    line = line.split(" ")
    cmd = line[0]
    if cmd == "Replace":
        current_char = line[1]
        new_char = line[2]
        new_string = ""
        for i in string:
            if i == current_char:
                new_string += new_char
            else:
                new_string += i
        string = new_string
        print(string)
    elif cmd == "Cut":
        start_idx = int(line[1])
        end_idx = int(line[2])
        # indexes are valid
        if 0 <= start_idx < len(string) and 0 <= end_idx < len(string):
            first_slice = string[:start_idx]
            second_slice = string[end_idx + 1:]
            new_string = first_slice + second_slice
            string = new_string
            print(string)
        else:
            print("Invalid indexes!")
    elif cmd == "Make":
        func = line[1]
        if func == "Upper":
            string = string.upper()
        elif func == "Lower":
            string = string.lower()
        print(string)
    elif cmd == "Check":
        substring = line[1]
        if substring in string:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")
    elif cmd == "Sum":
        start_idx = int(line[1])
        end_idx = int(line[2])
        # indexes are valid
        if 0 <= start_idx < len(string) and 0 <= end_idx < len(string):
            sum_values = 0
            substring = string[start_idx:end_idx + 1]
            for i in substring:
                sum_values += ord(i)
            print(sum_values)
        else:
            print("Invalid indexes!")