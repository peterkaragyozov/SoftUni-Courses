def solve(string):
    digits = ""
    letters = ""
    other = ""
    for ch in string:
        if ch.isdigit():
            digits += ch
        elif ch.isalpha():
            letters += ch
        else:
            other += ch
    print(digits)
    print(letters)
    print(other)

solve(input())


# Втори начин:

# def solve(string):
#     print("".join([ch for ch in string if ch.isdigit()]))
#     print("".join([ch for ch in string if ch.isalpha()]))
#     print("".join([ch for ch in string if not ch.isalnum()]))
#
#
# solve(input())