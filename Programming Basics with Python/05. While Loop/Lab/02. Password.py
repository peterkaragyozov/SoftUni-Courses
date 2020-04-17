username = input()
correct_password = input()

input_password = input()
while input_password != correct_password:
    input_password = input()

print(f"Welcome {username}!")