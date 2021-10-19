from collections import OrderedDict
from timeit import timeit


def create_dict():
    return {str(i): i for i in range(1000)}


def create_order_dict():
    return OrderedDict({str(i): i for i in range(1000)})


test1 = create_dict()
test2 = create_order_dict()

print('Dict: ' + str(timeit("create_dict()", globals=globals(), number=10000)))
print('OrderedDict: ' + str(timeit("create_order_dict()", globals=globals(), number=10000)))
print(f'создание словарей - OrderedDict в полтора раза медленнее\n')

print('Dict: ' + str(timeit("test1.popitem", globals=globals(), number=10000)))
print('OrderedDict: ' + str(timeit("test2.popitem", globals=globals(), number=10000)))
print(f'Удаление из словарей пары. Dict быстрее\n')

print('Dict: ' + str(timeit("test1.values", globals=globals(), number=10000)))
print('OrderedDict: ' + str(timeit("test2.values", globals=globals(), number=10000)))
print(f'Возвращение значений из словарей. Dict быстрее\n')

print('Dict: ' + str(timeit("test1.keys", globals=globals(), number=10000)))
print('OrderedDict: ' + str(timeit("test2.keys", globals=globals(), number=10000)))
print(f'Возвращение ключей из словарей. Dict быстрее\n')

print(f'В Python 3.6 и более поздних версиях нет смысла использовать OrderedDict')
