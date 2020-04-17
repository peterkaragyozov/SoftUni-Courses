destination = ""

while destination != "End":
    destination = input()
    if destination == "End":
        break
    else:
        current_sum = 0
        min_budget = float(input())
        while min_budget > current_sum:
            current_sum += float(input())
        if current_sum >= min_budget:
            print(f"Going to {destination}!")