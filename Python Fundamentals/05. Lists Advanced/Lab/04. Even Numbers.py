numbers = [int(n.strip()) for n in input().split(',')]
even_number_indexes = [index for index, number in enumerate(numbers) if number % 2 == 0]
print(even_number_indexes)


# string = input().split(", ")
# new_string = []
# for num in enumerate(string):
#     number = num
#     if int(number[1]) % 2 == 0:
#         index = number[0]
#         new_string.append(index)
# print(new_string)