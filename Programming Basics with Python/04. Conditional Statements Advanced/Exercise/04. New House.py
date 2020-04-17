type_flowers = input()
flowers_count = int(input())
budget = int(input())

price = 0

if type_flowers == "Roses":
    price = 5
    if flowers_count > 80:
        discount = 0.1 * price
        price = price - discount
    else:
        price = 5

elif type_flowers == "Dahlias":
    price = 3.80
    if flowers_count > 90:
        discount = 0.15 * price
        price = price - discount
    else:
        price = 3.80

elif type_flowers == "Tulips":
    price = 2.80
    if flowers_count > 80:
        discount = 0.15 * price
        price = price - discount
    else:
        price = 2.80

elif type_flowers == "Narcissus":
    price = 3
    if flowers_count < 120:
        discount = 0.15 * price
        price = price + discount
    else:
        price = 3

elif type_flowers == "Gladiolus":
    price = 2.50
    if flowers_count < 80:
        discount = 0.2 * price
        price = price + discount
    else:
        price = 2.50

total_price = price * flowers_count

sum = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flowers_count} {type_flowers} and {sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {sum:.2f} leva more.")