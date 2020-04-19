# n = int(input())
# for i in range(1, n + 1):
#     digits_sum = 0
#     for digit in str(i):
#         digits_sum += int(digit)
#     is_special = digits_sum in [5, 7, 11]
#     print(f"{i} -> {is_special}")

# Втори начин

# number = int(input())
# for num in range(1, number + 1):
#     sum_digits = 0
#     digits = num
#
#     while digits > 0:
#         sum_digits += digits % 10
#         digits = digits // 10
#
#     if (sum_digits == 5) or (sum_digits == 7) or (sum_digits == 11):
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")

# Трети начин

n = int(input())
for i in range(1, n + 1):
    digits_sum = 0
    for digit in str(i):
        digits_sum += int(digit)
    is_special = digits_sum == 5 or digits_sum == 7 or digits_sum == 11
    print(f"{i} -> {is_special}")