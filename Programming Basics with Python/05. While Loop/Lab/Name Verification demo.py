name = input()

is_name_correct = name == "admin"
while is_name_correct:
    print("Hello, " + name)
    name = input()
    is_name_correct = name == "admin"

print("loop ended")