followers_dict = {}

while True:
    line = input()
    if line == "Log out":
        print(f"{len(followers_dict)} followers")

        followers_dict = dict(sorted(followers_dict.items(), key=lambda x: (-x[1][0], x[0])))

        for k, v in followers_dict.items():
            print(f"{k}: {sum(v)}")

        break

    line = line.split(": ")
    cmd = line[0]
    username = line[1]

    if cmd == "New follower":
        if username not in followers_dict:
            followers_dict[username] = [0] * 2

    elif cmd == "Like":
        count = int(line[2])
        if username not in followers_dict:
            followers_dict[username] = [0] * 2
        followers_dict[username][0] += count

    elif cmd == "Comment":
        if username not in followers_dict:
            followers_dict[username] = [0] * 2
        followers_dict[username][1] += 1

    elif cmd == "Blocked":
        if username not in followers_dict:
            print(f"{username} doesn't exist.")
        else:
            del followers_dict[username]