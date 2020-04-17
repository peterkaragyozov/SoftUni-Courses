n = int(input())

left_sum = 0

for i in range(n): #само n, защото е ясно, че чете от 0 до n
    num = int(input())
    left_sum += num

right_sum = 0

for i in range(n):
    num = int(input())
    right_sum += num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")