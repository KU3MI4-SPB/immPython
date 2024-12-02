def cache_decorator(func):
    cache = {}

    def wrapper(number):
        if number in cache:
            return cache[number]
        result = func(number)
        cache[number] = result
        return result

    return wrapper


@cache_decorator
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(5))
