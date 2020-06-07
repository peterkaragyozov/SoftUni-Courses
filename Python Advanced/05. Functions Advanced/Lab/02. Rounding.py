def to_round_list(values):
    return [round(x) for x in values]


print(to_round_list(map(float, input().split(" "))))
# print(to_round_list([float (x) for x in input().split()]))