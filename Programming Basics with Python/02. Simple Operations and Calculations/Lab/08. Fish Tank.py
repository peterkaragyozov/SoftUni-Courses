length = int(input())
width = int(input())
height = int(input())

volume_percent = float(input())

volume = length * width * height
liters = volume * 0.001

percent = volume_percent * 0.01

final_liters = liters * (1 - percent)
print(f"{final_liters:.3f}")