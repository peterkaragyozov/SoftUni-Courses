import sys

name = input()
max_sum = -sys.maxsize
max_name = ""

while name != "STOP":
    sum_name = 0
    for letter in name:
        sum_name += ord(letter)
    if sum_name > max_sum:
        max_sum = sum_name
        max_name = name
    name = input()

print(f"Winner is {max_name} - {max_sum}!")