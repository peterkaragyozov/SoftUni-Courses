jury_members = int(input())
presentation = ""
total_sum_marks = 0
mark_count = 0

while presentation != "Finish":
    presentation = input()
    if presentation == "Finish":
        break
    sum_marks = 0
    for i in range(jury_members):
        current_mark = float(input())
        sum_marks += current_mark
        total_sum_marks += current_mark
        mark_count += 1
    average_mark = sum_marks / jury_members

    print(f"{presentation} - {average_mark:.2f}.")

print(f"Student's final assessment is {(total_sum_marks / mark_count):.2f}.")