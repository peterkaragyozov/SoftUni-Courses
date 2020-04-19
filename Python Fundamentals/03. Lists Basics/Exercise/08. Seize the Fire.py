fires_line = input().split("#")
water = int(input())

effort = 0
total_fire = 0
print("Cells:")
for tokens in fires_line:
    token = tokens.split(" = ")
    type_of_fire = token[0]
    value_of_cell = int(token[1])
    if type_of_fire == "High" and value_of_cell <= water:
        if 81 <= value_of_cell <= 125:
            water -= value_of_cell
            effort += 0.25 * value_of_cell
            total_fire += value_of_cell
            print(f" - {value_of_cell}")
    elif type_of_fire == "Medium" and value_of_cell <= water:
        if 51 <= value_of_cell <= 80:
            water -= value_of_cell
            effort += 0.25 * value_of_cell
            total_fire += value_of_cell
            print(f" - {value_of_cell}")
    elif type_of_fire == "Low" and value_of_cell <= water:
        if 1 <= value_of_cell <= 50:
            water -= value_of_cell
            effort += 0.25 * value_of_cell
            total_fire += value_of_cell
            print(f" - {value_of_cell}")


print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")