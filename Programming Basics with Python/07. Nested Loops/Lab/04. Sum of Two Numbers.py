start_number = int(input())
end_number = int(input())
magic_number = int(input())
count_combinations = 0
is_found_valid_combination = False

for first_number in range(start_number, end_number + 1):
    if is_found_valid_combination:
        break
    for second_number in range(start_number, end_number + 1):
        count_combinations += 1
        if first_number + second_number == magic_number:
            print(f"Combination N:{count_combinations} ({first_number} + {second_number} = {magic_number})")
            is_found_valid_combination = True
            break
if not is_found_valid_combination:
    print(f"{count_combinations} combinations - neither equals {magic_number}")