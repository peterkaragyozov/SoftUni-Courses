people = int(input())
capacity = int(input())

courses_num = int(people / capacity)
if people % capacity != 0:
    courses_num += 1
print(courses_num)

# Втори начин:

# import math
#
# people_num = int(input())
# capacity = int(input())
#
# courses_num = math.ceil(people_num / capacity)
# print(courses_num)