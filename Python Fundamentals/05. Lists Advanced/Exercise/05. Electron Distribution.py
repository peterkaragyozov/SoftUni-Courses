num = int(input())
electron_list = []
counter = 1

while sum(electron_list) < num:
    sum_numbers = 2 * counter ** 2
    electron_list.append(sum_numbers)
    counter += 1
if sum(electron_list) > num:
    electron_list.pop(-1)
    remaining_electrons = num - sum(electron_list)
    electron_list.append(remaining_electrons)
print(electron_list)