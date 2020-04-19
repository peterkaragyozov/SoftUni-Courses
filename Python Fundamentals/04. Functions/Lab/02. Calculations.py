def execute(a, b, operation):
    if operation == "multiply":
        return a * b
    elif operation == "add":
        return a + b
    elif operation == "divide":
        return a // b
    elif operation == "subtract":
        return a - b


operation = input()
a = int(input())
b = int(input())
print(execute(a, b, operation))