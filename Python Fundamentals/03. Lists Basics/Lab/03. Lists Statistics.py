num = int(input())

list_positives = []
list_negatives = []

count_positives = 0
sum_of_negatives = 0

for n in range(1, num + 1):
    current_num = int(input())
    if current_num >= 0:
        count_positives += 1
        list_positives.append(current_num)
    else:
        sum_of_negatives += current_num
        list_negatives.append(current_num)
print(list_positives)
print(list_negatives)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}")

# Втори начин с comprehension

# n = int(input())
#
# numbers = [int(input()) for _ in range(n)]
# positives = [n for n in numbers if n >= 0]
# negatives = [n for n in numbers if n < 0]
#
# print(positives)
# print(negatives)
#
# print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")