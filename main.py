def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

word = input()
@uppercase_decorator
def say_hi():
    return word
print(say_hi())

