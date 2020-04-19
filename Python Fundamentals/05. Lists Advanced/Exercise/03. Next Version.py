nums = list(map(int, input().split(".")))
nums[2] += 1

if nums[2] == 10:
    nums[2] = 0
    nums[1] += 1

if nums[1] == 10:
    nums[1] = 0
    nums[0] += 1

print(".".join(map(str, nums)))

# Втори начин:

# num = int(input().replace(".", ""))
# new_version = num + 1
# print(".".join(list(str(new_version))))