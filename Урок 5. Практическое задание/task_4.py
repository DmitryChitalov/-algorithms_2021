"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from collections import OrderedDict
from timeit import timeit


def move_to_end_dict(value_key):
    sample_dict[value_key] = sample_dict.pop(value_key)


def start_timeit(desc, odict_func, dict_func, repeat_value):
    print(f'Замер для функции {desc}:\n'
          f'ORDERED DICT: {timeit(odict_func, globals=globals(), number=repeat_value)}\n'
          f'DICT: {timeit(dict_func, globals=globals(), number=repeat_value)}\n')


sample_odict = OrderedDict([(index, index) for index in range(100)])
sample_dict = {index: index for index in range(100)}

start_timeit('Copy', 'sample_odict.copy()', 'sample_dict.copy()', 100000)
start_timeit('Get', 'sample_odict.get(100)', 'sample_dict.get(100)', 100000)
start_timeit('Items', 'sample_odict.items()', 'sample_dict.items()', 100000)
start_timeit('Keys', 'sample_odict.keys()', 'sample_dict.keys()', 100000)
start_timeit('Values', 'sample_odict.values()', 'sample_dict.values()', 100000)
# Специализированные команды
start_timeit('Move to end', 'move_to_end_dict(1)', 'sample_odict.move_to_end(1, True)', 1000)
start_timeit('Popitem', 'sample_odict.popitem()', 'sample_dict.popitem()', 100)

"""
Обычный словарь dict был разработан для быстрых операций добавления, извлечения и обновления данных.
Класс collections.OrderedDict() был разработан для частыx операций переупорядочивания. Эффективность использования 
памяти, скорость итераций и производительность операций обновления были второстепенными. - из документации

В большинстве своем, стандартные функции словаря работают немного быстрее упорядоченного словаря, но в случаях, если
требуется переупорядочить (удалить, поместить в конец), то упорядоченный словарь явно выигрывает у обычного, при этом, 
Popitem работает быстрее только на небольшом объеме данных, если приходится удалять большое количество ключей, то разницы
практически нет.
Считаю, что упорядоченные словари стоит использовать только в частных случаях, когда надо быстро удалить некоторое (небольшое)
количество элементов словаря, либо быстро переместить данные в конец. В целом, сомневаюсь, что эти преимущества стоят того, 
чтобы в нужный момент создавать упорядоченный словарь на основе словаря, потому-то скорее всего, на инициализацию
упорядоченного словаря может уйти больше времени, чем получим в результате его использования.

Замер для функции Copy:
ORDERED DICT: 0.7033126
DICT: 0.03974489999999997

Замер для функции Get:
ORDERED DICT: 0.0039244999999999974
DICT: 0.0035857999999999723

Замер для функции Items:
ORDERED DICT: 0.004590100000000041
DICT: 0.005294000000000021

Замер для функции Keys:
ORDERED DICT: 0.004582100000000033
DICT: 0.004319599999999979

Замер для функции Values:
ORDERED DICT: 0.005229299999999992
DICT: 0.00443019999999994

Замер для функции Move to end:
ORDERED DICT: 0.00014420000000003874
DICT: 4.379999999992723e-05

Замер для функции Popitem (10 элементов):
ORDERED DICT: 2.500000000016378e-06
DICT: 8.000000000008e-06

Замер для функции Popitem (100 элементов):
ORDERED DICT: 1.1299999999936361e-05
DICT: 1.2299999999965117e-05
"""
