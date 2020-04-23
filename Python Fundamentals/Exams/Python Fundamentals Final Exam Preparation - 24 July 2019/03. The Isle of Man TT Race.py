import re

pattern = r"^([#$%*&])([a-zA-Z]+)\1=(\d+)!!(.+)$"

while True:
    message = input()
    match = re.fullmatch(pattern, message)

    if match and len(match.group(4)) == int(match.group(3)):
        length = int(match.group(3))
        geohashcode = "".join([chr(ord(x) + length) for x in match.group(4)])
        racer = match.group(2)

        print(f"Coordinates found! {racer} -> {geohashcode}")
        break
    else:
        print("Nothing found!")