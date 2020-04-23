import re

pattern = r"@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+"

n = int(input())

for i in range(n):
    text = input()

    match = re.match(pattern, text)

    if match is None:
        print("Invalid barcode")
        continue

    barcode = match.group(1)

    if barcode.isalpha():
        product_group = "00"
    else:
        product_group = ""
        for i in barcode:
            if i.isdigit():
                product_group += i

    print(f"Product group: {product_group}")