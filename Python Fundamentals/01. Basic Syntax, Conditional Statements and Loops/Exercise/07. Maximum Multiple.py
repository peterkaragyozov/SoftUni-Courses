divisor = int(input())
bound = int(input())
largest_number = 0

for number in range(1, bound + 1):
    if number % divisor == 0:
        largest_number = number
print(largest_number)