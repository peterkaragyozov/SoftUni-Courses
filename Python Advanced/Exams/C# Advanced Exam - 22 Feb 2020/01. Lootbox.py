from collections import deque

box_queue = deque([int(x) for x in input().split()])
box_stack = [int(x) for x in input().split()]

collection_items = 0

while box_queue and box_stack:
    first_element = box_queue[0]
    last_element = box_stack[-1]
    summed_value = first_element + last_element

    if summed_value % 2 == 0:
        collection_items += summed_value
        box_queue.popleft()
        box_stack.pop()
    else:
        last_element = box_stack.pop()
        box_queue.append(last_element)

if not box_queue:
    print("First lootbox is empty")
if not box_stack:
    print("Second lootbox is empty")

if collection_items >= 100:
    print(f"Your loot was epic! Value: {collection_items}")
else:
    print(f"Your loot was poor... Value: {collection_items}")