new = list(map(int, input().split(" ")))

for i in range(int(input())):
    new.pop(new.index(min(new)))

print(new)