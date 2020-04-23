username = input()

while True:
    commands = input()
    if commands == "Sign up":
        break
    commands = commands.split(" ")
    cmd = commands[0]

    if cmd == "Case":
        if commands[1] == "lower":
            username = username.lower()
        else:
            username = username.upper()
        print(username)
    elif cmd == "Reverse":
        start = int(commands[1])
        end = int(commands[2])
        if (0 <= start < len(username)) and (0 <= end < len(username)):
            reversed_string = list(reversed(username[start:end + 1]))
            print("".join(reversed_string))
    elif cmd == "Cut":
        substring = commands[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif cmd == "Replace":
        char = commands[1]
        username = username.replace(char, "*")
        print(username)
    elif cmd == "Check":
        char = commands[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")