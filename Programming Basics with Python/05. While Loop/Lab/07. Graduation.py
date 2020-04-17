name = input()

grades_counter = 1
grades_sum = 0

while grades_counter <= 12:
    current_grade_final_mark = float(input())

    if current_grade_final_mark >= 4:
        grades_counter += 1
        grades_sum += current_grade_final_mark

average_grade = grades_sum / 12

print(f"{name} graduated. Average grade: {average_grade:.2f}")