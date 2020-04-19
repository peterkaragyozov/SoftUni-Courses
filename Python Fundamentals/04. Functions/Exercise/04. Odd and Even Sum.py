def odd_even_sum(single_number):
    sum_even = 0
    sum_odd = 0
    for digit in single_number:
        if int(digit) % 2 == 0 and int(digit) != 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


single_number = input()
print(odd_even_sum(single_number))