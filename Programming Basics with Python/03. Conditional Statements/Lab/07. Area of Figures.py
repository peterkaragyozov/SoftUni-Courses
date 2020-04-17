figure_type = input()

if figure_type == "square":
    side_a = float(input())
    area = side_a ** 2

elif figure_type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

elif figure_type == "circle":
    r = float(input())
    from math import pi
    area = pi * r ** 2

elif figure_type == "triangle":
    side_a = float(input())
    height = float(input())
    area = side_a * height / 2

print(f"{area:.3f}")