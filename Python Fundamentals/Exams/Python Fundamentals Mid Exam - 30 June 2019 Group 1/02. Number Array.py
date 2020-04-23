array_numbers = [int(i) for i in input().split(" ")]

while True:
    line = input().split(" ")
    if line[0] == "End":
        break
    command = line[0]
    sum_num = 0
    if command == "Switch":
        index = int(line[1])
        if 0 <= index < len(array_numbers):
            array_numbers[index] = -array_numbers[index]
    elif command == "Change":
        index = int(line[1])
        value = int(line[2])
        if 0 <= index < len(array_numbers):
            array_numbers[index] = value
    elif line[1] == "Negative":
        for num in range(len(array_numbers)):
            if array_numbers[num] < 0:
                sum_num += array_numbers[num]
        print(sum_num)
    elif line[1] == "Positive":
        for num in range(len(array_numbers)):
            if array_numbers[num] >= 0:
                sum_num += array_numbers[num]
        print(sum_num)
    elif line[1] == "All":
        for num in range(len(array_numbers)):
            sum_num += array_numbers[num]
        print(sum_num)

new_nums = []
for num in range(len(array_numbers)):
    if array_numbers[num] >= 0:
        new_nums.append(array_numbers[num])

positive_nums = [str(i) for i in new_nums]
print(" ".join(positive_nums))