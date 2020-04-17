town = input()
sales = float(input())
fee = 0

if sales >= 0 and (town == "Sofia" or town == "Varna" or town == "Plovdiv"):
    if town == "Sofia":
        if 0 <= sales <= 500:
            fee = 0.05
        elif 500 < sales <= 1000:
            fee = 0.07
        elif 1000 < sales <= 10000:
            fee = 0.08
        elif sales > 10000:
            fee = 0.12
        print(f"{(sales * fee):.2f}")
    elif town == "Varna":
        if 0 <= sales <= 500:
            fee = 0.045
        elif 500 < sales <= 1000:
            fee = 0.075
        elif 1000 < sales <= 10000:
            fee = 0.1
        elif sales > 10000:
            fee = 0.13
        print(f"{(sales * fee):.2f}")
    else:
        if 0 <= sales <= 500:
            fee = 0.055
        elif 500 < sales <= 1000:
            fee = 0.08
        elif 1000 < sales <= 10000:
            fee = 0.12
        elif sales > 10000:
            fee = 0.145
        print(f"{(sales * fee):.2f}")

else:
    print("error")