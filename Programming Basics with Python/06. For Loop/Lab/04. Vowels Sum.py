text = input().lower()
res_sum = 0

for index in range(0, len(text)):
    character = text[index]

    if character == "a":
        res_sum += 1
    elif character == "e":
        res_sum += 2
    elif character == "i":
        res_sum += 3
    elif character == "o":
        res_sum += 4
    elif character == "u":
        res_sum += 5

print(res_sum)