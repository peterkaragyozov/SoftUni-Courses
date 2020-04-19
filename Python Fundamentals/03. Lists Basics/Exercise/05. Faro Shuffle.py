# cards = input().split(" ")
# shuffles = int(input())
#
# for i in range(shuffles):
#     first_half = []
#     second_half = []
#     new_cards = []
#     for j in range(0, int(len(cards) / 2)):
#         first_half.append(cards[j])
#
#     for k in range(int(len(cards) / 2), len(cards)):
#         second_half.append(cards[k])
#
#     for m in range(len(first_half)):
#         new_cards.append(first_half[m])
#         new_cards.append(second_half[m])
#
#     cards = new_cards
# print(cards)


# Втори начин:
cards = input().split(" ")
shuffle_count = int(input())
mid = len(cards) // 2

for shuffle in range(shuffle_count):
    result = []
    for i in range(mid):
        result.append(cards[i])
        result.append(cards[i + mid])
    cards = result
print(result)