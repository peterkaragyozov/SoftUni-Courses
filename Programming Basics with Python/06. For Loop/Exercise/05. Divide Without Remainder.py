num_count = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0


for numbers_counter in range(num_count):
    current_num = int(input())
    if current_num % 4 == 0:
        count_p3 += 1
    if current_num % 3 == 0:
        count_p2 += 1
    if current_num % 2 == 0:
        count_p1 += 1



p1 = count_p1 / num_count * 100
p2 = count_p2 / num_count * 100
p3 = count_p3 / num_count * 100


print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")