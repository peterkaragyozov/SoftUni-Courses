tank_capacity = 255
n = int(input())

for i in range(n):
    tank_fill = int(input())
    if tank_capacity - tank_fill < 0:
        print("Insufficient capacity!")
    else:
        tank_capacity -= tank_fill
print(255 - tank_capacity)

# Втори начин:

# tank = 255
# tank_fill = 0
# n = int(input())
# current_fill = 0
#
# for i in range(n + 1):
#     if current_fill <= tank:
#         tank -= current_fill
#         tank_fill += current_fill
#     else:
#         print("Insufficient capacity!")
#     if i == n:
#         break
#     else:
#         current_fill = int(input())
# print(tank_fill)