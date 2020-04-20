def solve(bakery_str):
    values = bakery_str.split(" ")
    bakery = {}
    n = len(values)
    for i in range(0, n, 2):
        food = values[i]
        quantity = int(values[i + 1])
        bakery[food] = quantity
    print(bakery)

solve(input())