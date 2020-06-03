line = input()
result = [el for x in line.split("|")[::-1] for el in x.split()]
print(" ".join(result))