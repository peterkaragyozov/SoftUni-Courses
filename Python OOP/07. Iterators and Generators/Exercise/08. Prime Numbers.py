def get_primes(sequence):
    for element in sequence:
        if element < 2:
            continue
        is_prime = True
        for num in range(2, element):
            if element % num == 0:
                is_prime = False
                break
        if is_prime:
            yield element


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))