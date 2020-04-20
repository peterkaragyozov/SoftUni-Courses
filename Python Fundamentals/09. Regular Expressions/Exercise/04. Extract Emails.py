import re

text = input()

user_pattern = r"( |^)[a-z0-9]+([\.\-_][a-z0-9]+)*"
host_pattern = r"[a-z]+(-[a-z]+)*(\.[a-z]+(-[a-z]+)*)+"
pattern = rf"{user_pattern}@{host_pattern}"

matches = re.finditer(pattern, text)

for match in matches:
    mail = match[0].strip()
    print(mail)