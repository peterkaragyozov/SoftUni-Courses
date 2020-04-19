words = input().split(" ")
search_word = input()

palindrome_words = [word for word in words if word == word[::-1]]
occurrences_count = palindrome_words.count(search_word)

print(palindrome_words)
print(f"Found palindrome {occurrences_count} times")