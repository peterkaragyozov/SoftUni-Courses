def perfect(n):
    div = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            div += i
    if div == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect(number))


# Втори начин:
# def is_perfect(number):
#     divisors = []
#     for i in range(1, number):
#         if number % i == 0:
#             divisors.append(i)
#     return sum(divisors) == number
#
#
# number = int(input())
# if is_perfect(number):
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")