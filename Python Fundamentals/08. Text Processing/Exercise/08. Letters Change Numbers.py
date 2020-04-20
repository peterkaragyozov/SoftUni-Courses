def get_letter_position(letter):
    num = 96
    if letter.isupper():
        num = 64

    return ord(letter) - num


tokens = input().split()
total_sum = 0

for part in tokens:
    f = part[0]
    f_position = get_letter_position(f)
    l = part[-1]
    l_position = get_letter_position(l)
    num = int(part[1:-1])

    curr_res = 0
    if f.isupper():
        curr_res += num / f_position
    else:
        curr_res += num * f_position

    if l.isupper():
        curr_res -= l_position
    else:
        curr_res += l_position

    total_sum += curr_res
print(f"{total_sum:.2f}")