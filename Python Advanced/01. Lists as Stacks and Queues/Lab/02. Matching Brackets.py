def get_subexpressions(expression):
    s = []
    result = []
    for index in range(len(expression)):
        ch = expression[index]
        if ch == "(":
            s.append(index)
        elif ch == ")":
            start_index = s.pop()
            result.append(expression[start_index:index + 1])
    return result

for subexpression in get_subexpressions(input()):
    print(subexpression)