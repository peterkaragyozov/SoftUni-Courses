# 1. Read tickets count
tickets_count = int(input())

# 2. Iterate through all tickets
for ticket in range(tickets_count):
    # 2.1 Read ticket number value
    ticket_number = input()
    # 2.2 Get ticket number length
    ticket_number_length = len(ticket_number)
    # 2.3 Compare characters count
    # 2.3.1 4
    seat_number = ''
    if ticket_number_length == 4:
        first_character = ticket_number[0]
        first_character_ascii = ord(first_character)
        # 2.3.1.1 Check if first character is [A-Z] -> {1}{2}{3}
        if 65 <= first_character_ascii <= 90:
            seat_number = f'{ticket_number[0]}{ticket_number[1]}{ticket_number[2]}'
        else:
            # 2.3.1.2 if first character is not in [A-Z] -> {4}{2}{3}
            seat_number = f'{ticket_number[3]}{ticket_number[1]}{ticket_number[2]}'
    # 2.3.2 5 / 6 -> {1}{ascii of second}
    elif ticket_number_length == 5 or ticket_number_length == 6:
        second_character_ascii = ord(ticket_number[1])
        seat_number = f'{ticket_number[0]}{second_character_ascii}'

    print(f'Seat decoded: {seat_number}')
    # 2.4 Print seat number