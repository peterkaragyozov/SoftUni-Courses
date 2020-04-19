secret_message = input().split(" ")
decrypted_message = ""
for word in secret_message:
    first_letter = ""
    decrypted_word = []
    for character in word:
        if character.isdigit():
            first_letter += character
        else:
            decrypted_word.append(character)
    letter_ascii = chr(int(first_letter))
    decrypted_word.insert(0, letter_ascii)
    decrypted_word[1], decrypted_word[-1] = decrypted_word[-1], decrypted_word[1]
    decrypted_message += "".join(decrypted_word) + " "


print(decrypted_message)