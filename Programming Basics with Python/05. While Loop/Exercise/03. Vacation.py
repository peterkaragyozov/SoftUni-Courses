vacation_cost = float(input())
saved_money = float(input())

spending_counter = 0
days_passed = 0

while saved_money < vacation_cost:
    action_type = input()
    current_sum = float(input())
    days_passed += 1
    if action_type == "spend":
        spending_counter += 1
        if spending_counter == 5:
                print(f"You can't save the money.")
                print(days_passed)
                break
        if saved_money < current_sum:
                saved_money = 0
        else:
                saved_money -= current_sum
    elif action_type == "save":
        saved_money += current_sum
        spending_counter = 0

if saved_money >= vacation_cost:
    print(f"You saved the money for {days_passed} days.")
