tasks_with_priority = []
while True:
    to_do = input()
    if to_do == "End":
        break
    tokens = to_do.split("-")
    priority = int(tokens[0])
    notes = tokens[1]
    tasks_with_priority.append((priority, notes))

sorted_tasks = sorted(tasks_with_priority)
print([task[1] for task in sorted_tasks])