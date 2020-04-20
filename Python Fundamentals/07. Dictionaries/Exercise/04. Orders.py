def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


name_price = {}
name_quantity = {}

while True:
    line = input().split(" ")
    if line[0] == "buy":
        break
    name = line[0]
    price = float(line[1])
    quantity = int(line[2])

    validate_key_existing(name_price, name)
    name_price[name] = price

    validate_key_existing(name_quantity, name)
    name_quantity[name] += quantity

for key in name_price.keys():
    print(f"{key} -> {name_price[key] * name_quantity[key]:.2f}")