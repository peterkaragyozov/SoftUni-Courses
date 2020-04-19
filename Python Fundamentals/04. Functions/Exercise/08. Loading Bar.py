def show_progress(integer_num):
    progress = ""
    for digit in integer_num:
        if len(integer_num) > 2:
            progress = 10 * "%"
        else:
            progress = int(digit[0]) * "%"
            total_progress = 10 - int(digit[0])
            progress += total_progress * "."
        break

    if integer_num == "100":
        print(f"{integer_num}% Complete!")
        print(f"[{progress}]")
    else:
        print(f"{integer_num}% [{progress}]")
        print("Still loading...")


integer_num = input()
show_progress(integer_num)