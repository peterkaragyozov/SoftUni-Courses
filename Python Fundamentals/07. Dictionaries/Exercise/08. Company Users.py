def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


company_employees = {}
while True:
    line = input().split(" -> ")
    if line[0] == "End":
        sorted_company_employees = sorted(company_employees.items(), key=lambda x: x[0])
        for i in sorted_company_employees:
            print(f"{i[0]}")
            for l in i[1]:
                print(f"-- {l}")
        break

    company = line[0]
    employee = line[1]

    validate_key_existing(company_employees, company, [])
    if employee not in company_employees[company]:
        company_employees[company].append(employee)