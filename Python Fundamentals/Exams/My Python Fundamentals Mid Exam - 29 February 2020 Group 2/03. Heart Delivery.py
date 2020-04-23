neighbourhood_list = [int(home) for home in input().split("@")]
last_position = 0
while True:
    line = input()
    if line == "Love!":
        break
    line = line.split(" ")
    length = int(line[1])

    index = last_position + length
    if index >= len(neighbourhood_list):
        index = 0

    if neighbourhood_list[index] > 0:
        neighbourhood_list[index] -= 2
        if neighbourhood_list[index] == 0:
            print(f"Place {index} has Valentine's day.")
    else:
        print(f"Place {index} already had Valentine's day.")

    last_position = index

print(f"Cupid's last position was {last_position}.")

counter = 0
failed_houses = 0
for house in range(len(neighbourhood_list)):
    if neighbourhood_list[house] == 0:
        counter += 1
    else:
        failed_houses += 1
if counter == len(neighbourhood_list):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_houses} places.")