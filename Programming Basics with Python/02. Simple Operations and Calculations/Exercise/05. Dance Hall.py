L = float(input())
W = float(input())
A = float(input())

from math import floor

area_hall = (L * 100) * (W * 100)
area_A = A * A * 100 * 100
area_bench = area_hall / 10

empty_space = area_hall - area_A - area_bench

number_dancers = empty_space / (7000 + 40)

number_dancers_rounded = floor(number_dancers)

print(f"{number_dancers_rounded}")