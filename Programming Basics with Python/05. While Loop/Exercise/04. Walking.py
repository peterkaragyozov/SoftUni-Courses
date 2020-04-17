steps_walked = 0
goal = 10000
while steps_walked < goal:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        steps_walked += steps_to_home
        break
    else:
        current_steps_walked = int(command)
        steps_walked += current_steps_walked

if steps_walked >= goal:
    print(f"Goal reached! Good job!")
else:
    print(f"{goal - steps_walked} more steps to reach goal.")