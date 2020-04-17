hour = int(input())
minutes = int(input())

calculated_minutes = minutes + 15

if calculated_minutes >= 60:
    hour = hour + 1
    calculated_minutes = calculated_minutes - 60

if hour >= 24:
    hour = 0


if calculated_minutes < 10:
    print(f"{hour}:0{calculated_minutes}")

else:
    print(f"{hour}:{calculated_minutes}")
