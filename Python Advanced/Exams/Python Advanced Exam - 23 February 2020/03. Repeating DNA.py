def get_repeating_DNA(dna_string):
    result = []
    for i in range(len(dna_string) - 10):
        current = dna_string[i:i + 10]
        if current in dna_string[i + 1:] and current not in result:
            result.append(current)
    return result


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)

test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)