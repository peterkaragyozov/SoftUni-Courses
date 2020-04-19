# numbers = list(map(lambda x: int(x), input().split(", ")))
# beggars = int(input())
#
# beggars_list = [0] * beggars
#
# for i in range(len(numbers)):
#     element = numbers[i]
#     beggar_index = i % len(beggars_list)
#     beggars_list[beggar_index] += element
#
# print(beggars_list)


# Втори начин:

nums_str = input().split(", ")
count = int(input())
nums = []

for num in nums_str:
    nums.append(int(num))

result_sum = [0] * count

for i in range(len(nums)):
    index = i % count
    result_sum[index] += nums[i]
print(result_sum)

