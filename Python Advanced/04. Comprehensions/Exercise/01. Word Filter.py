words = input().split()
filtered_words = [x for x in words if len(x) % 2 == 0]
[print(x) for x in filtered_words]