num_count = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

for numbers_counter in range(num_count):
    current_num = int(input())
    if current_num < 200:
        count_p1 += 1
    elif 200 <= current_num <= 399:
        count_p2 += 1
    elif 400 <= current_num <= 599:
        count_p3 += 1
    elif 600 <= current_num <= 799:
        count_p4 += 1
    elif 800 <= current_num:
        count_p5 += 1


p1 = count_p1 / num_count * 100
p2 = count_p2 / num_count * 100
p3 = count_p3 / num_count * 100
p4 = count_p4 / num_count * 100
p5 = count_p5 / num_count * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
