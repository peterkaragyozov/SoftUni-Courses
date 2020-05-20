expression = input()
opening_parentheses = []

for char in expression:
    if char in "[{(":
        opening_parentheses.append(char)
    else:
        if opening_parentheses:
            if char == ")":
                if opening_parentheses[-1] == "(":
                    opening_parentheses.pop()
            elif char == "}":
                if opening_parentheses[-1] == "{":
                    opening_parentheses.pop()
            elif char == "]":
                if opening_parentheses[-1] == "[":
                    opening_parentheses.pop()
        else:
            print("NO")
            exit()

if opening_parentheses:
    print("NO")
else:
    print("YES")
