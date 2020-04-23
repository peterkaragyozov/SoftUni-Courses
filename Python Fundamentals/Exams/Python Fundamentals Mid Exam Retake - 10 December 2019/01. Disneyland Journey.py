journey_price = float(input())
months_num = int(input())
saved_money = 0
souvenir_money = 0
needed_money = 0

for month in range(1, months_num + 1):
    if month % 4 == 0:
        saved_money += 25 / 100 * saved_money
    if month % 2 != 0 and month != 1:
        saved_money -= 16 / 100 * saved_money
    saved_money += 25 / 100 * journey_price

if saved_money >= journey_price:
    souvenir_money = saved_money - journey_price
    print(f"Bravo! You can go to Disneyland and you will have {souvenir_money:.2f}lv. for souvenirs.")
else:
    needed_money = journey_price - saved_money
    print(f"Sorry. You need {needed_money:.2f}lv. more.")