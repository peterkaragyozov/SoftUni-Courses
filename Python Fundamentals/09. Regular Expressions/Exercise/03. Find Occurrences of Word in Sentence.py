import re

text = input()
word_search = input()
pattern = rf"\b{word_search}\b"

matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))