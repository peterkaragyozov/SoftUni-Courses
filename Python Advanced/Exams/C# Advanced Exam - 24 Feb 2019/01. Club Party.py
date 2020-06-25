from collections import deque

max_capacity = int(input())
line = input().split()

open_halls = deque()
reservations = deque()
while line:
    current_item = line.pop()
    if current_item.isalpha():
        open_halls.append(current_item)
    else:
        if open_halls:
            reservations.append(int(current_item))
            if sum(reservations) > max_capacity:
                line.append(str(reservations.pop()))
                print(f"{open_halls.popleft()} -> {', '.join([str(x) for x in reservations])}")
                reservations = []