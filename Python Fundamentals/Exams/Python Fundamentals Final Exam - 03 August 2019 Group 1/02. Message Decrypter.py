import re

pattern = r"^(\$|%)(?P<tag>[A-Z][a-z]{2,})\1:[ ]\[(?P<one>\d+)\]\|\[(?P<two>\d+)\]\|\[(?P<three>\d+)\]\|$"

n = int(input())

for i in range(n):
    text = input()
    match = re.match(pattern, text)

    if match is None:
        print("Valid message not found!")
    else:
        tag = match.group('tag')
        first_num = chr(int(match.group('one')))
        second_num = chr(int(match.group('two')))
        third_num = chr(int(match.group('three')))
        decrypted_message = first_num + second_num + third_num
        print(f"{tag}: {decrypted_message}")