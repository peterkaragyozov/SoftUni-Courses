name_list = input().split(", ")

while True:
    command = input().split(" ")

    if "Report" in command:
        break
    elif "Blacklist" in command:
        if len(command) >= 2:
            name = command[1]
            if name in name_list:
                i = name_list.index(name)
                name_list[i] = "Blacklisted"
                print(f"{name} was blacklisted.")
            else:
                print(f"{name} was not found.")
    elif "Error" in command:
        if len(command) >= 2:
            i = command[1]
            if len(i) == 1 and (48 <= ord(i) <= 57):
                i = int(i)
                if i < len(name_list):
                    name = name_list[i]
                    if name != "Blacklisted" and name != "Lost":
                        name_list[i] = "Lost"
                        print(f"{name} was lost due to an error.")
    elif "Change" in command:
        if len(command) >= 3:
            i = command[1]
            if len(i) == 1 and (48 <= ord(i) <= 57):
                i = int(i)
                if i < len(name_list):
                    current_name = name_list[i]
                    new_name = command[2]
                    print(f"{current_name} changed his username to {new_name}.")
                    name_list[i] = new_name

blacklisted_names_count = name_list.count("Blacklisted")
lost_names_count = name_list.count("Lost")

print(f"Blacklisted names: {blacklisted_names_count}")
print(f"Lost names: {lost_names_count}")
print(" ".join(name_list))