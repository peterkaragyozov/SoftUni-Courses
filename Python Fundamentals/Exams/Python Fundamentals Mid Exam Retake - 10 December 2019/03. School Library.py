line = input().split("&")
shelf = []

for i in range(len(line)):
    shelf.append(line[i])
while True:
    second_line = input()
    if second_line == "Done":
        break
    second_line = second_line.split(" | ")
    command = second_line[0]
    if command == "Add Book":
        book_name = second_line[1]
        if book_name in shelf:
            continue
        shelf.insert(0, book_name)
    elif command == "Take Book":
        book_name = second_line[1]
        if book_name in shelf:
            shelf.remove(book_name)
        continue
    elif command == "Swap Books":
        book_name = second_line[1]
        book_name_two = second_line[2]
        if (book_name in shelf) and (book_name_two in shelf):
            idx = shelf.index(book_name)
            idx_two = shelf.index(book_name_two)
            shelf[idx], shelf[idx_two] = shelf[idx_two], shelf[idx]
    elif command == "Insert Book":
        book_name = second_line[1]
        shelf.append(book_name)
    elif command == "Check Book":
        index = int(second_line[1])
        if index > len(shelf):
            continue
        print(shelf[index])

print(", ".join(shelf))