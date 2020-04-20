def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


def is_item_in_dict(items, item):
    return True if item in items else False


force_book = {}

while True:
    text = input()

    if text == "Lumpawaroo":
        break

    side = ""
    user = ""

    if " | " in text:
        args = text.split(" | ")
        side = args[0]
        user = args[1]

        all_users = [item for current_list in force_book.values() for item in current_list]

        if user in all_users:
            continue

        validate_key_existing(force_book, side, [])
        force_book[side].append(user)
    else:
        args = text.split(" -> ")
        user = args[0]
        side = args[1]

        side_of_user = ""
        for k, v in force_book.items():
            if user in v:
                side_of_user = k
                break

        if side_of_user != "":
            force_book[side_of_user].remove(user)

        validate_key_existing(force_book, side, [])
        force_book[side].append(user)
        print(f"{user} joins the {side} side!")

force_book = dict(sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])))

for k, v in force_book.items():
    if len(v) == 0:
        continue

    print(f"Side: {k}, Members: {len(v)}")

    for s in sorted(v):
        print(f"! {s}")