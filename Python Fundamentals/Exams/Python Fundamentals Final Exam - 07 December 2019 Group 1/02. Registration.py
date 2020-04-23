import re

username_pattern = r"U\$([A-Z][a-z]{2,})U\$"
password_pattern = r"P@\$([a-z]{5,}\d+)P@\$"

pattern = fr"{username_pattern}{password_pattern}"

n = int(input())
total_count = 0
for i in range(n):
    registration = input()
    match = re.match(pattern, registration)

    if match is None:
        print("Invalid username or password")
        continue
    total_count += 1
    print("Registration was successful")
    print(f"Username: {match[1]}, Password: {match[2]}")

print(f"Successful registrations: {total_count}")