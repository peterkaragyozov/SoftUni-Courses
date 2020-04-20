import re

pattern = r"(w{3}\.[a-zA-Z0-9\-]+(\.[a-z]+)+)"

while True:
    text = input()
    if not text:
        break

    matches = [x[0] for x in re.findall(pattern, text)]
    for match in matches:
        print(match)
