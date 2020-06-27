def list_manipulator(list, command, beg_or_end, *args):
    result_list = list

    if command == "add" and beg_or_end == "beginning":
        for el in range(len(args) - 1, - 1, - 1):
            result_list.insert(0, args[el])

    elif command == "add" and beg_or_end == "end":
        for el in range(len(args)):
            result_list.append(args[el])

    elif command == "remove" and beg_or_end == "beginning":
        if args:
            n = int(args[0])
            for _ in range(n):
                result_list.pop(0)
        else:
            result_list.pop(0)

    elif command == "remove" and beg_or_end == "end":
        if args:
            n = int(args[0])
            for _ in range(len(result_list), len(result_list) - n, - 1):
                result_list.pop()
        else:
            result_list.pop()

    return result_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))