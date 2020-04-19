def is_valid_password(password):
    password_is_valid = 0
    if 6 <= len(password) <= 10:
        password_is_valid += 1
    else:
        password_is_valid = 0
        print("Password must be between 6 and 10 characters")
    two_digits_count = 0
    is_valid = False

    for digit in password:
        if 48 <= ord(digit) <= 57 or 65 <= ord(digit) <= 90 or 97 <= ord(digit) <= 122:
            is_valid = True
        else:
            is_valid = False
            print("Password must consist only of letters and digits")
            break
        if 48 <= ord(digit) <= 57:
            two_digits_count += 1

    if is_valid == True:
        password_is_valid += 1
    if two_digits_count >= 2:
        password_is_valid += 1
    else:
        print("Password must have at least 2 digits")

    if password_is_valid == 3:
        print("Password is valid")


password = input()
is_valid_password(password)