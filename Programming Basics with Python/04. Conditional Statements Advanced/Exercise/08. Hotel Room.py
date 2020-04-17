month = input()
nights_count = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if nights_count > 14:
        discount_studio = 0.3
        discount_apartment = 0.1
        studio_price = studio_price - (discount_studio * studio_price)
        apartment_price = apartment_price - (discount_apartment * apartment_price)
    elif nights_count > 7:
        discount_studio = 0.05
        studio_price = studio_price - (discount_studio * studio_price)
    else:
        studio_price = 50
        apartment_price = 65


elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights_count > 14:
        discount_studio = 0.2
        discount_apartment = 0.1
        studio_price = studio_price - (discount_studio * studio_price)
        apartment_price = apartment_price - (discount_apartment * apartment_price)
    else:
        studio_price = 75.20
        apartment_price = 68.70

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if nights_count > 14:
        discount_apartment = 0.1
        apartment_price = apartment_price - (discount_apartment * apartment_price)
    else:
        studio_price = 76
        apartment_price = 77

total_stays_studio = nights_count * studio_price
total_stays_apartment = nights_count * apartment_price


print(f"Apartment: {total_stays_apartment:.2f} lv.")
print(f"Studio: {total_stays_studio:.2f} lv.")