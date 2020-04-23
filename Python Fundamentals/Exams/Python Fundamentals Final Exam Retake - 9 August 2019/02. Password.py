import re

pattern = r"^(.+)\>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|(.{3})\<\1$"

n = int(input())

for i in range(n):
    text = input()
    match = re.match(pattern, text)

    if match is None:
        print("Try another password!")
    else:
        encrypted_password = str(match.group(2)) + match.group(3) + match.group(4) + match.group(5)
        print(f"Password: {encrypted_password}")