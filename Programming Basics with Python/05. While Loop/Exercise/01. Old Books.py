book_name = input()
library_capacity = int(input())

searched_books_counter = 0
is_book_found = False
while searched_books_counter < library_capacity:
    current_book_name = input()
    if current_book_name.lower() == book_name.lower():
        is_book_found = True
        print(f"You checked {searched_books_counter} books and found it.")
        break
    searched_books_counter += 1

if not is_book_found:
    print(f"The book you search is not here!\nYou checked {library_capacity} books.")