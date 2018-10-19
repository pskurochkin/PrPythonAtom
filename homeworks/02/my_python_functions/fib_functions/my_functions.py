def cache_decorator(function):
    cache = {}

    def cached_function(arg):
        if arg in cache:
            return cache[arg]
        else:
            cache[arg] = function(arg)
            return cache[arg]

    return cached_function

@cache_decorator
def fib(n):
    if n > 2:
        return fib(n - 2) + fib(n - 1)
    else:
        return 1
