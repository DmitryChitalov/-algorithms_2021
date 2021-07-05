"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

usual_dict = {i: i for i in range(10)}
ord_dict = OrderedDict([(i, i) for i in range(10)])

def get_usual_dict(key):
    return usual_dict.get(key)


def get_ord_dict(key):
    return ord_dict.get(key)

print(f'Заполнение обычного словаря словаря - ', timeit('usual_dict', globals=globals()))
print(f'Заполнение OrderedDict - ', timeit('ord_dict', globals=globals()))

print(f'Получение элемента из обычного словаря словаря - ', timeit('get_usual_dict("key-100")', globals=globals(), number=1000000))
print(f'Получение элемента из OrderedDict - ', timeit('get_ord_dict("key-100")', globals=globals(), number=1000000))

# OrderedDict уступает по скорости обычному словарю, потому что был создан для быстрого переупорядочивания элементов,
# вопреки производительности, на базе Python, в отличии от обычного словаря на базе С. В итого, OrderedDict следует использовать для
#  специфичных функций: move_to_end(key, last=True), popitem(last=True)