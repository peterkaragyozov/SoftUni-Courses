import re

pattern = r"\b(_)([a-zA-Z0-9]+\b)"
text = input()

matches = re.findall(pattern, text)
variable_names = []
for match in matches:
    variable_names.append(match[1])

print(",".join(variable_names))