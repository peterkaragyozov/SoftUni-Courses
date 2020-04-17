number = int(input())
length = float(input())
width = float(input())

total_area_rectangle = number * (length + 2 * 0.30) * (width + 2 * 0.30)

area_stripe = (length / 2) ** 2

total_area_stripe = number * area_stripe

USD = total_area_rectangle * 7 + total_area_stripe * 9
BGN = USD * 1.85

print(f"{USD:.2f} USD")
print(f"{BGN:.2f} BGN")