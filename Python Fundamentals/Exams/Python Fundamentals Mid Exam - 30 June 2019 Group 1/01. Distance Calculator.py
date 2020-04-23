steps = int(input())
step_length = float(input()) / 100
target_distance = int(input())

steps_made = 0

for step in range(1, steps + 1):
    if step % 5 == 0:
        step = step_length - (30 / 100 * step_length)
    else:
        step = step_length
    steps_made += step

percentage = steps_made / target_distance * 100

print(f"You travelled {percentage:.2f}% of the distance!")