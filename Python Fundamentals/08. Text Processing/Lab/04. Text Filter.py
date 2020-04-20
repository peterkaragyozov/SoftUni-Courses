def text_filter(text, words):
    for word in words:
        text = text.replace(word, "*" * len(word))
    return text


words = input().split(", ")
text = input()

print(text_filter(text, words))