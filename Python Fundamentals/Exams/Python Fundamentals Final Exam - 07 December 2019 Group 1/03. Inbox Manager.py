users_dict = {}

while True:
    line = input()
    if line == "Statistics":
        print(f"Users count: {len(users_dict)}")
        sorted_users_dict = sorted(users_dict.items(), key=lambda x: (-len(x[1]), x[0]))
        for i in sorted_users_dict:
            print(f"{i[0]}")
            for l in i[1]:
                print(f"- {l}")
        break
    line = line.split("->")
    cmd = line[0]
    if cmd == "Add":
        username = line[1]
        if username in users_dict:
            print(f"{username} is already registered")
        elif username not in users_dict:
            users_dict[username] = []
    elif cmd == "Send":
        username = line[1]
        email = line[2]
        users_dict[username].append(email)
    elif cmd == "Delete":
        username = line[1]
        if username in users_dict:
            del users_dict[username]
        elif username not in users_dict:
            print(f"{username} not found!")