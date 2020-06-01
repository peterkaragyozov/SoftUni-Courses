def is_number_valid(number):
    return len([True for d in range(2, 11) if number % d == 0]) > 0


start_number = int(input())
end_number = int(input())
print([x for x in range(start_number, end_number + 1) if is_number_valid(x)])