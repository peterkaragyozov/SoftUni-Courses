text = input()

index = 0
res = ""
start_index = 0

while index < len(text):
    if text[index].isdigit():
        num_str = text[index]
        next_index = 1

        if index + 1 < len(text) and text[index + 1].isdigit():
            num_str += text[index + 1]
            next_index = 2

        num = int(num_str)
        res += text[start_index:index] * num

        if index + 1 >= len(text):
            break

        start_index = index + next_index
    index += 1

res = res.upper()
print(f"Unique symbols used: {len(set(res))}")
print(res)