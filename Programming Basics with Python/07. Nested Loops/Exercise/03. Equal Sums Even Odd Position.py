first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    current = str(number)

    sum_even = 0
    sum_odd = 0
    for index, digit in enumerate(current):
        if index % 2 == 0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)
    if sum_even == sum_odd:
        print(f"{number} ", end="")