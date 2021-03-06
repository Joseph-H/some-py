import urllib.error
import urllib.request

from functools import lru_cache, partial, singledispatch

"""
@lru_cache will “wrap a function with a memoizing callable that saves up to the maxsize most recent calls”
The function get_webpage will make http calls and the first time it happens the results will come back slowly
on subsequent calls, if the calls are the same, it will return them quickly as it has cached the result
"""


@lru_cache(maxsize=24)
def get_webpage(module):
    """
    Gets the specified Python module web page
    """
    webpage = "https://docs.python.org/3/library/{}.html".format(module)
    try:
        with urllib.request.urlopen(webpage) as request:
            return request.read()
    except urllib.error.HTTPError:
        return None


"""
partial is something that you can use to "save" the call of a function. example below
"""


def add(one, two):
    return one + two


# here saved is the invocation of add with 2 and 4 as arguments
saved = partial(add, 2, 4)
# when saved is executed then it executes the function
print(saved())

"""
Function overloading with singledispatch. Overloading only happens on type, though
"""


@singledispatch
def print_type(arg):
    raise NotImplementedError("Unsupported type")


@print_type.register(int)
def _(arg):
    print("Argument is of type ", type(arg))


@print_type.register(float)
@print_type.register(str)
def _(arg):
    # and you can stack types
    print("Argument is of type ", type(arg))


print_type(2)
print_type(2.0)
print_type("2")
