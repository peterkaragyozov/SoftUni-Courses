string = input()

for char in range(len(string)):
    if ord(string[char]) == 58:
        print(f":{string[char + 1]}")