def student_record(student, grade):
    if student not in grades_dict:
        grades_dict[student] = []
    grades_dict[student].append(f"{grade:.2f}")


num = int(input())
grades_dict = {}

for _ in range(num):
    student, grade = input().split(" ")
    student_record(student, float(grade))

for student, grades in grades_dict.items():
    average = sum([float(x) for x in grades]) / len(grades)
    print(f"{student} -> {' '.join(grades)} (avg: {average:.2f})")