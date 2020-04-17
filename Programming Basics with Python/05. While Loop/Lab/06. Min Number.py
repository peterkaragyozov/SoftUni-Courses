minimum_numbers_count = int(input())
counter = 0
smallest_number = 1000000000
while minimum_numbers_count > counter:
    current_number = int(input())

    if current_number < smallest_number:
        smallest_number = current_number
    counter += 1

print(smallest_number)