from math import floor

income = float(input())
average_grades = float(input())
minimal_salary = float(input())

social_scholarship = floor(minimal_salary * 0.35)
grades_scholarship = floor(average_grades * 25)


if income < minimal_salary and 5.5 > average_grades > 4.5:
   print(f"You get a Social scholarship {social_scholarship} BGN")

elif income < minimal_salary and average_grades >= 5.5:
    if social_scholarship > grades_scholarship:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {grades_scholarship} BGN")

elif average_grades >= 5.5:
    print(f"You get a scholarship for excellent results {grades_scholarship} BGN")

else:
    print("You cannot get a scholarship!")