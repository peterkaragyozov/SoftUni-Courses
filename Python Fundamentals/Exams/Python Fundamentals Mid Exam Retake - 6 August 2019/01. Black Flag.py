plunder_days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
accumulated_plunder = 0


for day in range(1, plunder_days + 1):
    if day % 3 == 0:
        accumulated_plunder += daily_plunder + 50 / 100 * daily_plunder
    else:
        accumulated_plunder += daily_plunder
    if day % 5 == 0:
        accumulated_plunder -= 30 / 100 * accumulated_plunder

if accumulated_plunder >= expected_plunder:
    print(f"Ahoy! {accumulated_plunder:.2f} plunder gained.")
else:
    percentage = (accumulated_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")