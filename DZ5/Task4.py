from timeit import default_timer
from collections import OrderedDict

some_dict = {}
some_ordered_dict = OrderedDict()
n = 10000


def time_decorator(some_func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = some_func(*args, **kwargs)
        print(f'Время выполенения функции {some_func.__name__} '
              f'составило {default_timer() - start}. ')

        return result

    return wrapper


@time_decorator
def fill_dict(dict, num):
    for i in range(num):
        dict[i] = i


@time_decorator
def fill_ordered_dict(dict, num):
    for i in range(num):
        dict[i] = i


@time_decorator
def change_dict(dict):
    for i in range(10000):
        dict.pop(i)
    for j in range(100, 200):
        dict[j] = 'fill'
    for k, v in dict.items():
        dict[k] = 'some value'


@time_decorator
def change_ordered_dict(dict):
    for i in range(10000):
        dict.pop(i)
    for j in range(100, 200):
        dict[j] = 'fill'
    for k, v in dict.items():
        dict[k] = 'some value'


fill_dict(some_dict, n)
fill_ordered_dict(some_ordered_dict, n)

change_dict(some_dict)
change_ordered_dict(some_ordered_dict)

test = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(test)
test.move_to_end('b', last=True)
print(test)
test.popitem(last=True)
print(test)
