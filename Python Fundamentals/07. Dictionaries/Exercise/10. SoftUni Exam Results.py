def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


language_submission = {}
username_points = {}

while True:
    cmd = input().split("-")
    if cmd[0] == "exam finished":
        break
    username = cmd[0]
    language = cmd[1]

    if cmd[1] == "banned":
        if username in username_points:
            del username_points[username]
        break
    points = int(cmd[2])
    validate_key_existing(language_submission, language)
    language_submission[language] += 1

    validate_key_existing(username_points, username)
    if points > username_points[username]:
        username_points[username] = points

print("Results:")
max_score = dict(sorted(username_points.items(), key=lambda x: (-x[1], x[0])))
print_dict(max_score, "{} | {}")

print("Submissions:")
lang_count = dict(sorted(language_submission.items(), key=lambda x: (-x[1], x[0])))
print_dict(lang_count, "{} - {}")