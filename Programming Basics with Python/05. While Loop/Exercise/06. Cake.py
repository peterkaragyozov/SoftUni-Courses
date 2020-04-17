cake_width = int(input())
cake_lenght = int(input())
remaining_pieces = cake_width * cake_lenght
needed_pieces = 0

while remaining_pieces >= 0:
    pieces_taken = input()
    if pieces_taken == "STOP":
        print(f"{remaining_pieces} pieces are left.")
        break
    else:
        pieces_taken = int(pieces_taken)
    remaining_pieces -= pieces_taken
if remaining_pieces <= 0:
    needed_pieces = abs(remaining_pieces)
    print(f"No more cake left! You need {needed_pieces} pieces more.")