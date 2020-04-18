import sys

current_num = 0

biggest_num = -sys.maxsize

for i in range(3):
    current_num = int(input())
    if current_num > biggest_num:
        biggest_num = current_num

print(biggest_num)