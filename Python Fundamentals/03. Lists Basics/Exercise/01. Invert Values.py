numbers_as_string = input().split(" ")
numbers = []

for number in numbers_as_string:
    numbers.append(int(number) * -1)

print(numbers)