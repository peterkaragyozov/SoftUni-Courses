max_price_clothes = 50.00
max_price_shoes = 35.00
max_price_accessories = 20.50

bought = []

item_prices = input().split("|")
budget = float(input())


for tokens in item_prices:
    token = tokens.split("->")
    item = token[0]
    price = float(token[1])
    if item == "Clothes":
        if price <= max_price_clothes and budget - price >= 0:
            budget -= price
            bought.append(price)
    elif item == "Shoes":
        if price <= max_price_shoes and budget - price >= 0:
            budget -= price
            bought.append(price)
    elif item == "Accessories":
        if price <= max_price_accessories and budget - price >= 0:
            budget -= price
            bought.append(price)

profit = 40 / 100 * sum(bought)
for i in range(len(bought)):
    print(f"{(bought[i] * 1.4):.2f}", end=" ")
print()
print(f'Profit: {profit:.2f}')

new_budget = budget + sum(bought) * 1.4
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")