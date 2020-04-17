budget = int(input())
season = input()
fishermen_count = int(input())

rental_price = 0
if season == "Spring":
    rental_price = 3000
elif season == "Summer" or season == "Autumn":
    rental_price = 4200
elif season == "Winter":
    rental_price = 2600

discount = 0
if fishermen_count <= 6:
    discount = 0.1
elif 7 <= fishermen_count <= 11:
    discount = 0.15
elif fishermen_count >= 12:
    discount = 0.25

discount_value = rental_price * discount
expenses = rental_price - discount_value

if fishermen_count % 2 == 0 and season != "Autumn":
    expenses = expenses - expenses * 0.05

if budget >= expenses:
    print(f"Yes! You have {(budget - expenses):.2f} leva left.")
else:
    print(f"Not enough money! You need {(expenses - budget):.2f} leva.")