budget = float(input())
price_flour_kg = float(input())

cozonacs_count = 0
colored_eggs_count = 0


price_pack_eggs = 75 / 100 * price_flour_kg
price_milk_liter = 25 / 100 * price_flour_kg + price_flour_kg

while budget >= 0:
    if (price_pack_eggs + price_flour_kg + price_milk_liter / 4) > budget:
        break
    budget -= price_pack_eggs + price_flour_kg + price_milk_liter / 4

    cozonacs_count += 1
    colored_eggs_count += 3
    if cozonacs_count % 3 == 0:
        colored_eggs_count -= cozonacs_count - 2

print(f"You made {cozonacs_count} cozonacs! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")