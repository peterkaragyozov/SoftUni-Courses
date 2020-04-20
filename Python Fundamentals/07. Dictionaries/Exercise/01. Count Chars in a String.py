# input_line = input()
# characters_dict = {}
#
# for char in input_line:
#     if char == " ":
#         continue
#
#     if char not in characters_dict:
#         characters_dict[char] = 0
#     characters_dict[char] += 1
#
# for (key, value) in characters_dict.items():
#     print(f"{key} -> {value}")

# Втори начин:

def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))

text = input()
my_dict = {}

for ch in text:
    if ch == " ":
        continue

    validate_key_existing(my_dict, ch)
    my_dict[ch] += 1

print_dict(my_dict, "{} -> {}")