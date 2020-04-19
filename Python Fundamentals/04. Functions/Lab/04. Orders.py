def order(product, quantity):
    if product == "coffee":
        return 1.50 * quantity
    elif product == "water":
        return 1.00 * quantity
    elif product == "coke":
        return 1.40 * quantity
    elif product == "snacks":
        return 2.00 * quantity


product = input()
quantity = int(input())
print(f"{order(product, quantity):.2f}")


# Втори начин:
def find_price_per_unit(product):
    if product == "coffee":
        return 1.5
    if product == "water":
        return 1.0
    if product == "coke":
        return 1.4
    if product == "snacks":
        return 2.0


def get_order_total(product, quantity):
    price_per_unit = find_price_per_unit(product)
    if price_per_unit is None:
        return 0.0
    return price_per_unit * quantity


product = input()
quantity = int(input())

print(f"{get_order_total(product, quantity):.2f}")