string = input().split(" ")
new_string = []
for word in string:
    new_word = []
    for char in word:
        new_word.append(chr(ord(char) + 3))
    new_word = ''.join(new_word)
    new_string.append(new_word)

print('#'.join(new_string))