n = int(input())

evenSum = 0
oddSum = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        evenSum += num

    else:
        oddSum += num

if evenSum == oddSum:
    print(f"Yes\nSum = {evenSum}")
else:
    print(f"No\nDiff = {abs(evenSum - oddSum)}")