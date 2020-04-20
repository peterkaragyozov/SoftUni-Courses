address = input().split(".")
extension = address[1]
file = address[0]
file_name = ""
for ch in range(len(file) - 1, 0, - 1):
    if file[ch] == chr(92):
        break
    file_name += file[ch]
print(f"File name: {''.join(list(reversed(file_name)))}")
print(f"File extension: {extension}")