change = float(input())
change_balance = int(change * 100)
returned_coins_count = 0

while change_balance > 0:
    times_coin_in_balance = 0
    if change_balance >= 200:
        times_coin_in_balance = change_balance // 200
        returned_coins_count += times_coin_in_balance
        change_balance -= times_coin_in_balance * 200
    elif change_balance >= 100:
        returned_coins_count += 1
        change_balance -= 100
    elif change_balance >= 50:
        returned_coins_count += 1
        change_balance -= 50
    elif change_balance >= 20:
        times_coin_in_balance = change_balance // 20
        returned_coins_count += times_coin_in_balance
        change_balance -= times_coin_in_balance * 20
    elif change_balance >= 10:
        returned_coins_count += 1
        change_balance -= 10
    elif change_balance >= 5:
        returned_coins_count += 1
        change_balance -= 5
    elif change_balance >= 2:
        times_coin_in_balance = change_balance // 2
        returned_coins_count += times_coin_in_balance
        change_balance -= times_coin_in_balance * 2
    elif change_balance >= 1:
        returned_coins_count += 1
        change_balance -= 1

print(returned_coins_count)