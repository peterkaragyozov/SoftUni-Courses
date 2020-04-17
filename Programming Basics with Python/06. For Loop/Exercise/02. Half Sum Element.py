import sys

numbers_count = int(input())
max_num = -sys.maxsize
num_sum = 0


for i in range(numbers_count):
    num = int(input())
    num_sum += num
    if num > max_num:
        max_num = num
    num_sum2 = num_sum - max_num
if max_num == num_sum2:
    print(f"Yes\nSum = {num_sum2}")
else:
    print(f"No\nDiff = {abs(max_num - num_sum2)}")