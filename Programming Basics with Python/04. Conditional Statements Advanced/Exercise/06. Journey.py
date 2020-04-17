budget = float(input())
season = (input())

destination = ""
sleeping = ""
expenses = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        sleeping = "Camp"
        expenses = 0.3 * budget
    elif season == "winter":
        sleeping = "Hotel"
        expenses = 0.7 * budget

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        sleeping = "Camp"
        expenses = 0.4 * budget
    elif season == "winter":
        sleeping = "Hotel"
        expenses = 0.8 * budget

elif budget > 1000:
    destination = "Europe"
    sleeping = "Hotel"
    expenses = 0.9 * budget


print(f"Somewhere in {destination}")
print(f"{sleeping} - {expenses:.2f}")