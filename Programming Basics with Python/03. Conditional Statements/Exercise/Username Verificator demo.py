username = input()
email = input()

correct_username = "PeterKaragyozov"
is_username_correct = username == correct_username
if is_username_correct:
    if email == "s.simeonova@softuni.bg":
        print("Welcome, " + correct_username)
elif username == "admin":
    print("Hello, admin!")
elif username == "administrator":
    print("Hello, admin!")
else:
    print("Incorrect username. Please try again.")


#Друг начин

username = input()
email = input()

correct_username = "PeterKaragyozov"
is_username_correct = username == correct_username
if is_username_correct and email == "s.simeonova@softuni.bg":
    print("Welcome, " + correct_username)
elif username == "admin":
    print("Hello, admin!")
elif username == "administrator":
    print("Hello, admin!")
else:
    print("Incorrect username. Please try again.")