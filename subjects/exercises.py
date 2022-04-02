# from typing import Dict, List

"""
exercise 1:
Write a decorator which wraps functions to log function arguments and the return value on each call.
Provide support for both positional and named arguments (your wrapper function should take both
*args and **kwargs and print them both):
>>> @logged
... def func(*args):
...
return 3 + len(args)
>>> func(4, 4, 4)
you called func(4, 4, 4)
it returned 6
6
"""


def logged(func):
    def wrapper(*args):
        print(f"you called {func.__name__}{args}")
        result = func(*args)
        print(f"it returned {result}")
        print(result)
        return result

    return wrapper


class Logged:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print(f"you called {self.func.__name__}{args}")
        result = self.func(*args)
        print(f"it returned {result}")
        print(result)
        return result


# @logged
@Logged
def func(*args) -> int:
    return 3 + len(args)


"""
Exercise 2:
Write a decorator to cache function invocation results. Store pairs arg:result in a dictionary in an attribute of the function object. The function being memoized is:

def fibonacci(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
"""


def memorize(func):
    func.cache = {}

    def wrapper(n):
        try:
            ans = func.cache[n]
        except KeyError:
            ans = func.cache[n] = func(n)
        return ans

    return wrapper


@memorize
def fibonacci(n: int):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(13)


"""
fibonacci generator
"""


def fib(nterms):

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        assert nterms > 0, "Please enter a positive integer"

    # if there is only one term, return n1
    elif nterms == 1:
        yield (n1)

    # generate fibonacci sequence
    else:
        while count < nterms:
            yield (n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
