cards = input().split(":")
deck = []

while True:
    comm = input().split(" ")
    if comm[0] == "Ready":
        break
    elif comm[0] == "Shuffle" and comm[1] == "deck":
        deck.reverse()
    elif comm[0] == "Add":
        card = comm[1]
        if card in cards:
            deck.append(card)
        else:
            print("Card not found.")
    elif comm[0] == "Insert":
        card = comm[1]
        ind = int(comm[2])
        if card in cards and 0 <= ind < len(deck):
            deck.insert(ind, card)
        else:
            print("Error!")
    elif comm[0] == "Remove":
        card = comm[1]
        if card in deck:
            deck.remove(card)
        else:
            print("Card not found.")
    elif comm[0] == "Swap":
        card1 = comm[1]
        card2 = comm[2]
        ind1 = deck.index(card1)
        ind2 = deck.index(card2)
        deck[ind1], deck[ind2] = deck[ind2], deck[ind1]

print(" ".join(deck))