def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))

resources = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    validate_key_existing(resources, resource)
    resources[resource] += quantity

print_dict(resources, "{} -> {}")