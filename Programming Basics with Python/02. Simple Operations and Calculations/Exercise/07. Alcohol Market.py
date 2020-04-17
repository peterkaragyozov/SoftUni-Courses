price_whisky = float(input())

beer = float(input())
wine = float(input())
rakia = float(input())
whisky = float(input())

price_rakia = price_whisky / 2
price_wine = price_rakia - (40 / 100 * price_rakia)
price_beer = price_rakia - (80 / 100 * price_rakia)

quantity = (beer * price_beer) + (wine * price_wine) + (rakia * price_rakia) + (whisky * price_whisky)

print(f"{quantity:.2f}")