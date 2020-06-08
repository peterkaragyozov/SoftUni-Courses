from collections import deque

males_stack = [int(x) for x in input().split(" ")]
females_deque = deque([int(x) for x in input().split(" ")])

matches_count = 0

while males_stack and females_deque:
    current_male = males_stack[-1]
    current_female = females_deque[0]

    if current_male <= 0 or current_female <= 0:
        if current_male <= 0:
            males_stack.pop()
        if current_female <= 0:
            females_deque.popleft()
        continue

    if current_male % 25 == 0 or current_female % 25 == 0:
        if current_male % 25 == 0:
            males_stack.pop()
            if males_stack:
                males_stack.pop()
        if current_female % 25 == 0:
            females_deque.popleft()
            if females_deque:
                females_deque.popleft()
        continue

    if current_male == current_female:
        matches_count += 1
        males_stack.pop()
        females_deque.popleft()
    elif current_male != current_female:
        females_deque.popleft()
        males_stack[-1] -= 2

print(f"Matches: {matches_count}")

if males_stack:
    print(f"Males left: {', '.join([str(x) for x in males_stack[::-1]])}")
else:
    print("Males left: none")

if females_deque:
    print(f"Females left: {', '.join([str(x) for x in females_deque])}")
else:
    print("Females left: none")