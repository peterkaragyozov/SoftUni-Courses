password = input()

key = "s3cr3t!P@ssw0rd"

if password == key:
    print("Welcome")

else:
    print("Wrong password!")



    #Втори начин

username = input()
correct_username = "PeterKaragyozov"
is_username_correct = username == correct_username

if is_username_correct:
    print("Welcome, " + correct_username)