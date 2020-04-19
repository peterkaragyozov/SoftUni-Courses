first_num = int(input())
second_num = int(input())
third_num = int(input())
fourth_num = int(input())

sum_num = first_num + second_num
divided_num = int(sum_num / third_num)
final_num = divided_num * fourth_num

# Друг вариант:
# sum_num = (first_num + second_num) // third_num * fourth_num

print(final_num)


# Втори начин:

# num_sum = 0
#
# for i in range(4):
#     num = int(input())
#     if i < 2:
#         num_sum += num
#     elif i == 2:
#         num_sum = int(num_sum / num)
#     elif i == 3:
#         num_sum = num_sum * num
# print(num_sum)