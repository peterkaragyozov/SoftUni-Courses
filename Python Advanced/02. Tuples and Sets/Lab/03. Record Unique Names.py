names = set()
n = int(input())

for _ in range(n):
    names.add(input())

for name in names:
    print(name)


#   Second way:

# n = int(input())
# names = {input() for _ in range(n)}
# [print(name) for name in names]