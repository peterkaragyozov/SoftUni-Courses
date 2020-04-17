record = float(input())
distance = float(input())
speed = float(input())

from math import floor

time_needed = speed * distance

resistance = floor(distance / 15)
total_resistance = resistance * 12.5

total_time_swimmer = time_needed + total_resistance

if total_time_swimmer < record:
    print(f"Yes, he succeeded! The new world record is {total_time_swimmer:.2f} seconds.")

else:
    print(f"No, he failed! He was {(total_time_swimmer - record):.2f} seconds slower.")
