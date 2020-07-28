def vowel_filter(function):
    def wrapper():
        result = function()
        vowels = {"a", "e", "i", "u", "o"}
        return [x for x in result if x in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
