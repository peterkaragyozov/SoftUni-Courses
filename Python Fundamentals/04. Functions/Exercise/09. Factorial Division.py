def factorial(num):
    fact_multiplication = 1
    for i in range(1, num + 1):
        fact_multiplication = i * fact_multiplication

    return fact_multiplication


num = int(input())
num1 = factorial(num)

num = int(input())
num2 = factorial(num)

result = num1 / num2
print(f"{result:.2f}")