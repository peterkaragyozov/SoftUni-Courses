speed_input = float(input())

if speed_input <= 10:
    speed = "slow"
elif speed_input <= 50:
    speed = "average"
elif speed_input <= 150:
    speed = "fast"
elif speed_input <= 1000:
    speed = "ultra fast"
else:
    speed = "extremely fast"

print(speed)