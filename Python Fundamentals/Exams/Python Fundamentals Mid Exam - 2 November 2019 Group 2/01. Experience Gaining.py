needed_experience = float(input())
experience_earned = 0
battle_count = int(input())

for battle in range(1, battle_count + 1):
    current_experience = float(input())
    if battle % 3 == 0:
        experience_earned += current_experience + 15 / 100 * current_experience
    elif battle % 5 == 0:
        experience_earned += current_experience - 10 / 100 * current_experience
    else:
        experience_earned += current_experience

    if experience_earned >= needed_experience:
        break

if experience_earned >= needed_experience:
    print(f"Player successfully collected his needed experience for {battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {(needed_experience - experience_earned):.2f} more needed.")