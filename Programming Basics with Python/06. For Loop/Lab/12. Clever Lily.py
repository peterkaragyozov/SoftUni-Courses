years = int(input())
machine_price = float(input())
toy_price = int(input())

toys_count = 0
money_amount = 0

for year in range(1, years + 1):
    if year % 2 == 0:
        money_amount += year / 2 * 10
        money_amount -= 1
    else:
        toys_count += 1

toys_price = toys_count * toy_price
total_amount = toys_price + money_amount

if total_amount >= machine_price:
    print(f"Yes! {(total_amount - machine_price):.2f}")
else:
    print(f"No! {abs(total_amount - machine_price):.2f}")