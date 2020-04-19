line = input()
name_food_limit = {}

while line != "Last Info":
    token = line.split(":")
    command = token[0]
    animal = token[1]
    daily_food_limit = int(token[2])
    area = token[3]
    if command == "Add":
        if animal in name_food_limit:
            name_food_limit[animal][0] += daily_food_limit
        else:
            name_food_limit[animal] = [daily_food_limit, area]
    if command == "Feed":
        if animal in name_food_limit:
            name_food_limit[animal][0] -= daily_food_limit
            if name_food_limit[animal][0] <= 0:
                name_food_limit.pop(animal)
                print(f"{animal} was successfully fed")
    line = input()
sorted_dict = dict(sorted(name_food_limit.items(), key=lambda animal_food_limit: (animal_food_limit[1], animal_food_limit[0]), reverse= True))
print("Animals:")
for (key, value) in sorted_dict.items():
    print(f"{key} -> {value}g")


