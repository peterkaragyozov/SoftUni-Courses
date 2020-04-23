import re

pattern = r"^(?P<artist>[A-Z][a-z' ]+):(?P<song>[A-Z ]+)"

while True:
    text = input()
    if text == "end":
        break
    matches = re.match(pattern, text)

    if matches == None:
        print("Invalid input!")
        continue

    artist = matches.group("artist")
    song = matches.group("song")

    key = len(artist)

    encrypted_message = ""
    for l in text:
        if l == " " or l == "'":
            encrypted_message += l
            continue
        if l == ":":
            encrypted_message += "@"
            continue

        if ord(l) + key > ord("z"):
            encrypted_message += chr(96 + (key - (122 - ord(l))))
        elif ord(l.capitalize()) + key > ord("Z"):
            encrypted_message += chr(64 + (key - (90 - ord(l))))
        else:
            encrypted_message += chr(ord(l) + key)

    print(f"Successful encryption: {encrypted_message}")