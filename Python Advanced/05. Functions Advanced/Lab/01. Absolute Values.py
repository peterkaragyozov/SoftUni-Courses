def to_abs_list(values):
    return [abs(x) for x in values]


print(to_abs_list(map(float, input().split(" "))))

# Second Way:
# numbers = [abs(float(x)) for x in input().split()]
# print(numbers)