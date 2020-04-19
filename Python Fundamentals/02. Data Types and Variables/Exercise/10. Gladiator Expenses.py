lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
sum_expenses = 0

shield_counter = 0

for fight in range (1, lost_fights_count + 1):

    if fight % 2 == 0:
        sum_expenses += helmet_price
        #helmet broken
        if fight % 3 == 0:
            sum_expenses += shield_price
            shield_counter += 1
            #shield also broken
            if shield_counter % 2 == 0 and shield_counter != 0:
                sum_expenses += armor_price
                #armor needs repair
    if fight % 3 == 0:
        sum_expenses += sword_price
        #sword broken

print(f"Gladiator expenses: {sum_expenses:.2f} aureus")