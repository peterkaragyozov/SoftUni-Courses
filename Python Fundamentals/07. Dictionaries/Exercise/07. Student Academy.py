def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


students_count = int(input())
students = {}

for i in range(students_count):
    student = input()
    grade = float(input())

    validate_key_existing(students, student, [])
    students[student].append(grade)

average_grades = {}

for k, v in students.items():
    average_grade = sum(v) / len(v)

    if average_grade < 4.5:
        continue

    average_grades[k] = average_grade

average_grades = dict(sorted(average_grades.items(), key=lambda x: -x[1]))
print_dict(average_grades, "{} -> {:.2f}")