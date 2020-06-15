def fix_calendar(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    return numbers


numbers = [6, 4, 3, 2, 5, 1, 7, 9, 8]
fixed = fix_calendar(numbers)
print(fixed)
