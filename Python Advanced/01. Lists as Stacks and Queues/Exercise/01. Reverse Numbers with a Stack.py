stack = input().split(" ")
reversed_stack = []

for character in range(len(stack), 0, - 1):
    if stack:
        character = stack.pop()
        reversed_stack.append(character)

print(' '.join(reversed_stack))