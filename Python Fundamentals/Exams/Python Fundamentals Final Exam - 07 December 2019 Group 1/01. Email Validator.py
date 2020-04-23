email = input()
new_email = []

while True:
    command = input()
    if command == "Complete":
        break
    command = command.split(" ")
    cmd = command[0]
    if cmd == "Make":
        if command[1] == "Upper":
            email = email.upper()
            print(email)
        elif command[1] == "Lower":
            email = email.lower()
            print(email)
    elif cmd == "GetDomain":
        count = int(command[1])
        print(email[-3:])
    elif cmd == "GetUsername":
        if "@" in email:
            idx = email.index("@")
            print(email[:idx])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif cmd == "Replace":
        char = command[1]
        for i in range(len(email)):
            if email[i] == char:
                new_email.append("-")
            else:
                new_email.append(email[i])
        print("".join(new_email))
    elif cmd == "Encrypt":
        for i in range(len(email)):
            encrypted_symb = ord(email[i])
            print(encrypted_symb, end=" ")