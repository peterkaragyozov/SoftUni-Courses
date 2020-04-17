text = "word"

text_length = len(text)

for pos in range(text_length):
    print(text[pos])


#втори начин
text = "word"

text_length = len(text)

for char in text:
    print(char)

#трети начин
text = "word"

text_length = len(text)

for pos, char in enumerate(text):
    print(pos, char)