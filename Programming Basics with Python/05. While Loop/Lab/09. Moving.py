width = int(input())
lenght = int(input())
height = int(input())

space_volume = width * lenght * height
volume_taken = 0

while volume_taken < space_volume:
    input_text = input()
    if input_text == "Done":
        print(f"{space_volume - volume_taken} Cubic meters left.")
        break
# 2.1 if input is a number -> move boxes
    boxes_count = int(input_text)
    needed_volume = boxes_count
    volume_taken += needed_volume
# 2.1.1 if free space is not enough -> print cubic meters needed
if volume_taken > space_volume:
    print(f"No more free space! You need {volume_taken - space_volume} Cubic meters more.")
