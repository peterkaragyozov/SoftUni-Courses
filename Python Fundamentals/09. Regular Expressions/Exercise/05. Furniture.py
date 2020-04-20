import re

pattern = r">>(?P<item>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<count>\d+)"

bought_items = []
total = 0

while True:
    current_item = input()
    if current_item == "Purchase":
        break

    match = re.finditer(pattern, current_item)

    for element in match:
        bought_items.append(element.group("item"))
        total += float(element.group("price")) * int(element.group("count"))

print("Bought furniture:")
for item in bought_items:
    print(item)
print(f"Total money spend: {total:.2f}")