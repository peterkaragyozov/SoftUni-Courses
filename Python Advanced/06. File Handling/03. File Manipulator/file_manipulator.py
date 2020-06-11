import os

while True:
    input_line = input().split("-")
    command = input_line[0]

    if command == "End":
        break

    elif command == "Create":
        file_name = input_line[1]
        with open(file_name, "w") as file:
            file.write("")

    elif command == "Add":
        file_name = input_line[1]
        content = input_line[2]
        with open(file_name, "a") as file:
            file.write(content)
            file.write("\n")

    elif command == "Replace":
        file_name = input_line[1]
        old_string = input_line[2]
        new_string = input_line[3]

        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                text = file.read()
            text = text.replace(old_string, new_string)
            with open(file_name, "w") as file:
                file.write(text)
        else:
            print("An error occurred")

    elif command == "Delete":
        file_name = input_line[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")