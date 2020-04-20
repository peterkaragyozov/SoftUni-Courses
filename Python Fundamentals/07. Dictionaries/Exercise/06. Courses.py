def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))

courses = {}
while True:
    line = input().split(" : ")
    if line[0] == "end":
        break
    course = line[0]
    name = line[1]
    validate_key_existing(courses, course, [])
    courses[course].append(name)

courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))
for k, v in courses.items():
    courses_num = len(v)
    print(f"{k}: {courses_num}")
    for item in range(len(v)):
        v = sorted(v, reverse=True)
        print(f"-- {v.pop()}")