days = int(input())
bakers = int(input())

#ot edin sladkar za edin den
cakes = int(input()) * 45
waffles = int(input()) * 5.80
pancakes = int(input()) * 3.20

bakers_day_production = bakers * (cakes + waffles + pancakes)

total_campaign_production = days * bakers_day_production

profit = total_campaign_production - (1 / 8 * total_campaign_production)

print(f"{profit:.2f}")