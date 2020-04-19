num = int(input())
word = input()

my_list = []

for n in range(num):
    current_string = input()
    my_list.append(current_string)
print(my_list)

for i in range(len(my_list) - 1, -1, -1):
    element = my_list[i]
    if word not in element:
        my_list.remove(element)

print(my_list)

# Втори начин:

# n = int(input())
# word = input()
# strings = [input() for _ in range(n)]
#
# print(strings)
# print([string for string in strings if word in string])

