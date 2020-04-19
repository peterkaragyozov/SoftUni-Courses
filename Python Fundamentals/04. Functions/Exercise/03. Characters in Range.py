def fn(start, end):
    res = ""
    for i in range(ord(start) + 1, ord(end)):
        char = chr(i)
        res += chr(i) + " "

    return res

start = input()
end = input()
result = fn(start, end)
print(result)

# Втори начин
# character_one = input()
# character_two = input()
#
#
# def fn(character_one, character_two):
#     string = []
#     for i in range(ord(character_one) + 1, ord(character_two)):
#         char = chr(i)
#         string.append(char)
#
#     print(" ".join(string))
#
# fn(character_one, character_two)