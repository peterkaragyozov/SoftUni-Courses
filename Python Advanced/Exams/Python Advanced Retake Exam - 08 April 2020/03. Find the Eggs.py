def find_strongest_eggs(*args):
    sequence, num = args[0], args[1]
    sub_lists = [sequence[i::num] for i in range(num)]
    strongest_eggs = []

    for ll in sub_lists:
        middle = int(len(ll) / 2)
        first_half = ll[:middle]
        second_half = ll[middle + 1:]

        if ll[middle - 1] < ll[middle] > ll[middle + 1]:
            if [True for i, j in zip(first_half, second_half) if i < j]:
                strongest_eggs.append(ll[middle])
    return strongest_eggs


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
