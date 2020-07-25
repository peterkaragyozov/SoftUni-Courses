from itertools import permutations


def possible_permutations(my_list):
    for permutation in permutations(my_list):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]