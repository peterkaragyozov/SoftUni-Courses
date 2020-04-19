# num = int(input())
#
# even_list = []
# odd_list = []
# negative_list = []
# positive_list = []
#
# for n in range(num):
#     current_integer = int(input())
#     if current_integer % 2 == 0:
#         even_list.append(current_integer)
#     else:
#         odd_list.append(current_integer)
#     if current_integer >= 0:
#         positive_list.append(current_integer)
#     else:
#         negative_list.append(current_integer)
#
# command = input()
# if command == "even":
#     print(even_list)
# elif command == "odd":
#     print(odd_list)
# elif command == "positive":
#     print(positive_list)
# elif command == "negative":
#     print(negative_list)


# Втори начин:

# def is_even(number):
#     return number % 2 == 0
# def is_odd(number):
#     return number % 2 != 0
# def is_negative(number):
#     return number < 0
# def is_positive(number):
#     return number >= 0
#
# n = int(input())
# numbers = [int(input()) for _ in range(n)]
# command = input()
#
# FILTERS_MAP = {
#     "even": is_even,
#     "odd": is_odd,
#     "positive": is_positive,
#     "negative": is_negative,
# }
#
# filter_fn = FILTERS_MAP[command]
# print([n for n in numbers if filter_fn(n)])

# Трети начин:

n = int(input())
numbers = [int(input()) for _ in range(n)]
command = input()
filtered_numbers = []

for number in numbers:
    if command == "even" and number % 2 == 0:
        filtered_numbers.append(number)
    elif command == "odd" and number % 2 != 0:
        filtered_numbers.append(number)
    elif command == "positive" and number >= 0:
        filtered_numbers.append(number)
    elif command == "negative" and number < 0:
        filtered_numbers.append(number)
print(filtered_numbers)