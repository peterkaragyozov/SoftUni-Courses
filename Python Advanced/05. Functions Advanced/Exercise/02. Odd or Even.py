command = input()
numbers = list(map(int, input().split()))
# numbers = [int(x) for x in input().split()]
result = 0

if command == "Odd":
    result = sum(filter(lambda x: x % 2 == 1, numbers)) * len(numbers)
    #     print(sum([x for x in numbers if x % 2 != 0]) * len(numbers))
else:
    result = sum(filter(lambda x: x % 2 == 0, numbers)) * len(numbers)
    #     print(sum([x for x in numbers if x % 2 == 0]) * len(numbers))

print(result)