"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict

test_dict = {'key_1': 1, 'key_2': 2, 'key_3': 3}
test_o_dict = OrderedDict([('key_1', 1), ('key_2', 2), ('key_3', 3)])

print('Создание и заполнение')
print('dict:       ', timeit("test_dict = {'key_1': 1, 'key_2': 2, 'key_3': 3}", globals=globals(), number=10000))
print('OrderedDict:',
      timeit("test_o_dict = OrderedDict([('key_1', 1), ('key_2', 2), ('key_3', 3)])", globals=globals(), number=10000))
print()
print('Взятие элемента по ключу')
print('dict:       ', timeit("test_dict['key_2']", globals=globals(), number=10000))
print('OrderedDict:', timeit("test_o_dict['key_2']", globals=globals(), number=10000))

# Результат работы программы
#
# Создание и заполнение
# dict:        0.0013517000000000043
# OrderedDict: 0.004952199999999997
#
# Взятие элемента по ключу
# dict:        0.0003495999999999985
# OrderedDict: 0.00034929999999999684
#
# OrderedDict создаётся и заполняется в несколько раз дольше чем обычный словарь
# Взятие элемента по ключу выполняется с одинаковой скоростью
#
# Использование OrderedDict в Python 3.6 и более поздних версиях не имеет смысла
