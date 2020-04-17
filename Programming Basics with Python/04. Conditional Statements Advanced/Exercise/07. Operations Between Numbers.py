first_num = int(input())
second_num = int(input())
operation_symbol = input()

output = ""

if operation_symbol == "+":
    result = first_num + second_num
    output = f"{first_num} {operation_symbol} {second_num} = {result} - "
    if result % 2 == 0:
        output += "even"
    else:
        output += "odd"

elif operation_symbol == "-":
    result = first_num - second_num
    output = f"{first_num} {operation_symbol} {second_num} = {result} - "
    if result % 2 == 0:
        output += "even"
    else:
        output += "odd"

elif operation_symbol == "*":
    result = first_num * second_num
    output = f"{first_num} {operation_symbol} {second_num} = {result} - "
    if result % 2 == 0:
        output += "even"
    else:
        output += "odd"

elif operation_symbol == "/" and second_num != 0:
    result = first_num / second_num
    output = f"{first_num} {operation_symbol} {second_num} = {result:.2f}"

elif operation_symbol == "%" and second_num != 0:
    result = first_num % second_num
    output = f"{first_num} {operation_symbol} {second_num} = {result}"

elif (operation_symbol == "/" or operation_symbol == "%") and second_num == 0:
    output = f"Cannot divide {first_num} by zero"

print(output)