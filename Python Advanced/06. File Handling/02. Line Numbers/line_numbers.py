new_content = ""

with open("text.txt", "r") as file:
    for index, line in enumerate(file):
        letters_count = len([x for x in line if x.isalpha()])
        punctuation_count = 0
        for char in line:
            if char in "-,.!?'\";:":
                punctuation_count += 1

        new_content += f"Line {index + 1}: {line[:-1]} ({letters_count})({punctuation_count})\n"

with open("output.txt", "w") as file:
    file.write(new_content)


