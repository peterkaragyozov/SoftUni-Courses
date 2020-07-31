from functools import wraps


def even_parameters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        even_nums = [x for x in args if isinstance(x, int) and x % 2 == 0]
        if len(even_nums) == len(args):
            result = func(*args, **kwargs)
            return result
        return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
