import re

pattern = r"(^|(?<=\s))(?P<number>-?\d+([.]\d+)?)($|(?=\s))"

text = input()

matches = re.finditer(pattern, text)

numbers = [match.group("number") for match in matches]
print(" ".join(numbers))

# for match in matches:
#     print(match.group("number"))