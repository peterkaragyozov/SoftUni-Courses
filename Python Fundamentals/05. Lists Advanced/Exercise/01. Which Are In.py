string_one = input().split(", ")
string_two = input().split(", ")
new_string = []

for word in string_one:
    for substring in string_two:
        if word in substring and word not in new_string:
            new_string.append(word)

print(new_string)

#Втори начин:
# words = input().split(", ")
# string = input()
# res_list = []
#
# for word in words:
#     if word in string:
#         res_list.append(word)
# print(res_list)

# Трети начин:
# words = input().split(", ")
# string = input()
# res_list = [word for word in words if word in string]
# print(res_list)