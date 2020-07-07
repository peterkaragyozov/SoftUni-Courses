# Bad practice:

x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)

# Good practice:

x = "global"


def outer():
    def inner(x):
        new_x = f"nonlocal {x}"
        print("inner:", new_x)
        return new_x

    def change_global():
        return "global: changed!"

    x = "local"
    print("outer:", x)
    x = inner()
    print("outer:", x)

    return change_global()


print(x)
x = outer()
print(x)