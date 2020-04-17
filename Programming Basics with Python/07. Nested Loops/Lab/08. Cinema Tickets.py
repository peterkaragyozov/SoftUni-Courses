# до получаване на Finish -> четем заглавия
movie_name = input()
count_all_tickets = 0
count_all_students_tickets = 0
count_all_standard_tickets = 0
count_all_kids_tickets = 0

while movie_name != "Finish":
    free_seats = int(input())
    # докато не получим End -> четем типа на билета
    booked_seats = 0
    ticket_type = input()
    while ticket_type != "End":
        booked_seats += 1
        count_all_tickets += 1
        if ticket_type == "student":
            count_all_students_tickets += 1
        elif ticket_type == "standard":
            count_all_standard_tickets += 1
        elif ticket_type == "kid":
            count_all_kids_tickets += 1
        if booked_seats == free_seats:
            break
        ticket_type = input()
    percent = booked_seats / free_seats * 100
    print(f"{movie_name} - {percent:.2f}% full.")
    movie_name = input()

print(f"Total tickets: {count_all_tickets}")

percent_student_tickets = count_all_students_tickets / count_all_tickets * 100
print(f"{percent_student_tickets:.2f}% student tickets.")

percent_standard_tickets = count_all_standard_tickets / count_all_tickets * 100
print(f"{percent_standard_tickets:.2f}% standard tickets.")

percent_kids_tickets = count_all_kids_tickets / count_all_tickets * 100
print(f"{percent_kids_tickets:.2f}% kids tickets.")