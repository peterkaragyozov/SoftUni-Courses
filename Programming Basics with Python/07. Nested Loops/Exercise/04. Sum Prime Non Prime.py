text = input()

sum_prime_numbers = 0
sum_nonprime_numbers = 0

while text != "stop":
    current_num = int(text)
    if current_num < 0:
        print("Number is negative.")
        text = input()
        continue

    is_prime = True
    for i in range(2, current_num):
        if (current_num % i) == 0:
            sum_nonprime_numbers += current_num
            is_prime = False
            break
    if is_prime:
        sum_prime_numbers += current_num

    text = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_nonprime_numbers}")