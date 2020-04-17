number = int(input())

if number <= 100:
    bonus = 5
elif number > 1000:
    bonus = 10 / 100 * number
elif number > 100:
    bonus = 20 / 100 * number

if number % 2 == 0:
    bonus2 = 1
elif number % 10 == 5:
    bonus2 = 2
else:
    bonus2 = 0

total_points = number + bonus + bonus2

print(bonus + bonus2)
print(total_points)