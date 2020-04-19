snowballs_num = int(input())
snowball_value = 0
snowball_snow = 0
snowball_time = 0
snowball_quality = 0

for snowball in range(1, snowballs_num + 1):
    current_snowball_snow = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())
    current_snowball_value = int((current_snowball_snow / current_snowball_time) ** current_snowball_quality)
    if snowball_value < current_snowball_value:
        snowball_value = current_snowball_value
        snowball_snow = current_snowball_snow
        snowball_time = current_snowball_time
        snowball_quality = current_snowball_quality

print(f"{snowball_snow} : {snowball_time} = {snowball_value} ({snowball_quality})")