employee_one_efficiency = int(input()) #per hour
employee_two_efficiency = int(input())
employee_three_efficiency = int(input())
people_count = int(input())


three_employees_efficiency_per_hour = employee_one_efficiency + employee_two_efficiency + employee_three_efficiency


counter = 0
while people_count > 0:
    if counter % 4 == 0:
        counter += 1
    else:
        people_count -= three_employees_efficiency_per_hour
        if people_count <= 0:
            break
        counter += 1

print(f"Time needed: {counter}h.")