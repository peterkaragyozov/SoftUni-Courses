def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


parking = {}

num = int(input())
for i in range(num):
    line = input().split(" ")
    command = line[0]
    username = line[1]
    if command == "register":
        license_plate = line[2]
        if username not in parking:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")

    elif command == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]

print_dict(parking, "{} => {}")