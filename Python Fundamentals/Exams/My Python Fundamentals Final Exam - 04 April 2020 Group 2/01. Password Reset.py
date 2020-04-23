password = input()

while True:
    line = input()
    if line == "Done":
        print(f"Your password is: {password}")
        break
    line = line.split(" ")
    cmd = line[0]

    if cmd == "TakeOdd":
        new_password = ""
        for i in range(len(password)):
            if i % 2 != 0:
                new_password += password[i]
        password = new_password
        print(password)

    elif cmd == "Cut":
        index = int(line[1])
        length = int(line[2])

        substring = password[index:index + length]
        password = password.replace(substring, "", 1)
        print(password)

    elif cmd == "Substitute":
        substring = line[1]
        substitute = line[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")