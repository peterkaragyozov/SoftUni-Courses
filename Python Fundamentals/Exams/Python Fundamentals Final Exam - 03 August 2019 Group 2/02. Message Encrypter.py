import re

pattern = r"(\*|@)(?P<tag>[A-Z][a-z]{2,})\1:[ ]\[(?P<one>[a-zA-Z])\]\|\[(?P<two>[a-zA-Z])\]\|\[(?P<three>[a-zA-Z])\]\|$"

n = int(input())

for i in range(n):
    text = input()
    match = re.search(pattern, text)

    if match is None:
        print("Valid message not found!")
    else:
        tag = match.group('tag')
        first_char = str(ord(match.group('one')))
        second_char = str(ord(match.group('two')))
        third_char = str(ord(match.group('three')))
        decrypted_message = f"{first_char} {second_char} {third_char}"
        print(f"{tag}: {decrypted_message}")