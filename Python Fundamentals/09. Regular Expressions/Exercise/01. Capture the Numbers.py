import re

pattern = r"\d+"

text = input()

while True:
    if not text:
        break

    matches = re.findall(pattern, text)
    for match in matches:
        print(match, end=" ")
    text = input()