budget = float(input())
extras_count = int(input())
single_clothing_price = float(input())

decor_price = budget * 0.1

total_clothing_price = extras_count * single_clothing_price

if extras_count > 150:
    # discount = single_clothing_price * 0.1
    # total_clothing_price = total_clothing_price - discount
    total_clothing_price = total_clothing_price * 0.9

total_expenses = decor_price + total_clothing_price

if total_expenses <= budget:
    print("Action!")
    print(f"Wingard starts filming with {(budget - total_expenses):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {( total_expenses - budget):.2f} leva more.")
