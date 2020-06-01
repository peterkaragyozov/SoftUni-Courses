text = input()
vowels = {'a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I'}

sans_vowels = [ch for ch in text if ch not in vowels]
print("".join(sans_vowels))