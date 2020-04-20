strings = input().split()
result = ""
for word in range(len(strings)):
    multi_string = strings[word] * len(strings[word])
    result += multi_string
print(result)