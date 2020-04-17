type_year = input()
holidays_count_not_weekends = int(input())
weekends_vladi_hometown = int(input())

from math import floor

if weekends_vladi_hometown > 0:
    weekends_avaliable = 48 - weekends_vladi_hometown
    sofia_saturday_games = 3/4 * weekends_avaliable

    holidays_games = holidays_count_not_weekends * 2/3
    sofia_total = holidays_games + sofia_saturday_games
    total_year = sofia_total + weekends_vladi_hometown

    if type_year == "leap":
        total_year = total_year + 15 / 100 * total_year

    elif type_year == "normal":
        total_year = total_year
    print(f"{floor(total_year)}")


else:
    weekends_avaliable = 48
    sofia_saturday_games = 3/4 * weekends_avaliable

    holidays_games = holidays_count_not_weekends * 2/3
    sofia_total = holidays_games + sofia_saturday_games

    total_year = sofia_total

    if type_year == "leap":
        total_year = total_year + 15 / 100 * total_year
    elif type_year == "normal":
        total_year = total_year

    print(f"{floor(total_year)}")