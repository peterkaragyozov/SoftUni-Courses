days_count = int(input())
room = input()
rating = input()

price = 0
discount = 0
nights = days_count - 1

if nights < 10:
    if room == "room for one person":
        price = 18.00
        discount = 0
    elif room == "apartment":
        price = 25.00
        discount = 0.3
    elif room == "president_apartment":
        price = 35.00
        discount = 0.1

elif 10 <= nights <= 15:
    if room == "room for one person":
        price = 18.00
        discount = 0
    elif room == "apartment":
        price = 25.00
        discount = 0.35
    elif room == "president_apartment":
        price = 35.00
        discount = 0.15


elif nights > 15:
    if room == "room for one person":
        price = 18.00
        discount = 0
    elif room == "apartment":
        price = 25.00
        discount = 0.5
    elif room == "president apartment":
        price = 35.00
        discount = 0.2

price1 = nights * price * (1 - discount)

if rating == "positive":
    final_price = price1 + 0.25 * price1
elif rating == "negative":
    final_price = price1 - 0.1 * price1

print(f"{final_price:.2f}")