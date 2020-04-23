import math

daily_biscuits_amount_per_worker = int(input())
workers_count = int(input())
monthly_competing_factory_production = int(input())

monthly_production = 0

for day in range(1, 31):
    daily_production = daily_biscuits_amount_per_worker * workers_count
    if day % 3 == 0:
        daily_production = math.floor(75 / 100 * daily_production)
    monthly_production += daily_production


print(f"You have produced {monthly_production} biscuits for the past month.")

if monthly_production > monthly_competing_factory_production:
    difference = monthly_production - monthly_competing_factory_production
    percentage = difference / monthly_competing_factory_production * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    difference = monthly_competing_factory_production - monthly_production
    percentage = difference / monthly_competing_factory_production * 100
    print(f"You produce {percentage:.2f} percent less biscuits.")