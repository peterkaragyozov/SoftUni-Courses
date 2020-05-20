# 5 4 8 6 3 8 7 7 9
# 16
clothes_stack = [int(x) for x in input().split(" ")]
rack_capacity = int(input())
rack = 0
racks_num = 1

while clothes_stack:
    clothing = clothes_stack.pop()
    if rack + clothing <= rack_capacity:
        rack += clothing
    else:
        racks_num += 1
        rack = 0
        clothes_stack.append(clothing)

print(f"{racks_num}")