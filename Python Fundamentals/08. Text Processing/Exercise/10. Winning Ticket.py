tickets = input().split(",")


def find(ticket_fnc, showup_fnc):
    new_string_1 = showup_fnc[0][0] * showup_fnc[1]
    new_string_2 = showup_fnc[0][1] * showup_fnc[1]

    if new_string_1 in ticket_fnc[:10] and new_string_2 in ticket_fnc[10:]:
        return True


for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) == 20:  # Valid ticket
        first_part = ticket[0:10]
        second_part = ticket[10:len(ticket)]
        a_showups = first_part.count("@"), second_part.count("@")
        hashtag_showups = first_part.count("#"), second_part.count("#")
        dollar_showups = first_part.count("$"), second_part.count("$")
        xor_showups = first_part.count("^"), second_part.count("^")
        showups = [(a_showups, "@"), (hashtag_showups, "#"), (dollar_showups, "$"), (xor_showups, "^")]

        if 10 >= a_showups[0] >= 6 and 10 >= a_showups[1] >= 6 and find(ticket, showups[0]):
            if a_showups[0] == 10 and a_showups[1] == 10:
                print(f'ticket "{ticket}" - 10@ Jackpot!')
            else:
                print(f'ticket "{ticket}" - {min(a_showups)}@')
        elif 10 >= dollar_showups[0] >= 6 and 10 >= dollar_showups[1] >= 6 and find(ticket, showups[2]):
            if dollar_showups[0] == 10 and dollar_showups[1] == 10:
                print(f'ticket "{ticket}" - 10$ Jackpot!')
            else:
                print(f'ticket "{ticket}" - {min(dollar_showups)}$')
        elif 10 >= hashtag_showups[0] >= 6 and 10 >= hashtag_showups[1] >= 6 and find(ticket, showups[1]):
            if hashtag_showups[0] == 10 and hashtag_showups[1] == 10:
                print(f'ticket "{ticket}" - 10# Jackpot!')
            else:
                print(f'ticket "{ticket}" - {min(hashtag_showups)}#')
        elif 10 >= xor_showups[0] >= 6 and 10 >= xor_showups[1] >= 6 and find(ticket, showups[3]):
            if xor_showups[0] == 10 and xor_showups[1] == 10:
                print(f'ticket "{ticket}" - 10^ Jackpot!')
            else:
                print(f'ticket "{ticket}" - {min(xor_showups)}^')
        else:
            print(f'ticket "{ticket}" - no match')

    else:
        print("invalid ticket")