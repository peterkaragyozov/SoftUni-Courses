def is_palindrome(num_str):
    reversed_num = num_str[::-1]

    return True if num_str == reversed_num else False


def is_palindrome_two(num_str):
    length = len(num_str)
    is_palindrome = True

    for i in range(length // 2):
        if num_str[i] != num_str[length - 1 - i]:
            is_palindrome = False
            break

    return is_palindrome


nums = input().split(", ")

for num in nums:
    print(is_palindrome_two(num))