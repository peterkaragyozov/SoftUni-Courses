trip_cost = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

income_puzzles = puzzles_count * 2.60
income_talking_dolls = dolls_count * 3
income_teddy_bears = teddy_bears_count * 4.10
income_minions = minions_count * 8.20
income_trucks = trucks_count * 2

total_income = income_puzzles + income_talking_dolls + income_teddy_bears + income_minions + income_trucks

total_count = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count

if total_count >= 50:
    with_discount = total_income - (25 / 100 * total_income)
    remained_money = with_discount - (10 / 100 * with_discount)
else:
    earnings = total_income
    remained_money = earnings - (10 / 100 * earnings)

surplus = abs(remained_money - trip_cost)

if remained_money >= trip_cost:
    print(f"Yes! {surplus:.2f} lv left.")
else:
    print(f"Not enough money! {surplus:.2f} lv needed.")