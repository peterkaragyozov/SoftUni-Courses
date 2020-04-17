num = input()

for digit in reversed(num):
    number_to_digit = int(digit)
    if number_to_digit == 0:
        print("ZERO")
        continue
    symbol = chr(number_to_digit + 33)
    for i in range(1, number_to_digit + 1):
        print(symbol, end ="")
    print()