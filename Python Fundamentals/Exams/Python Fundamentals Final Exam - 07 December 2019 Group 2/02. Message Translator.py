import re

n = int(input())
pattern = r"!([A-Z][a-z]{2,})!:\[([a-zA-Z]{8,})\]"

for i in range(n):
    line = input()
    match = re.match(pattern, line)
    if match is None:
        print("The message is invalid")
    else:
        command = match[1]
        message = match[2]
        encrypted_message = []
        for char in message:
            encrypted_message.append(str(ord(char)))
        print(f"{command}: {' '.join(encrypted_message)}")