"""
Задача с основ: Определить элементы списка, не имеющие повторений.

Первая функция возвращает новый список, сгенерированный через
list comprehension.
Вторая - объект-итератор, сгенерированный
функцией filter, и каждое следующее значение будет
выдаваться по запросу, значительно экоромя
время выполнения и используемую память.
(аналогично map)

Функция doubles_check_1:
Время выполнения: 4.9561485 сек.
Использованная память: 0.0078125 Mib.

Функция doubles_check_2:
Время выполнения: 0.21962940000000053 сек.
Использованная память: 0.0 Mib.
"""
from random import randint
from task_1 import time_memo_prof

num_list = [randint(0, 1000) for i in range(20000)]


@time_memo_prof
def doubles_check_1(lst):
    return [el for el in lst if lst.count(el) == 1]


@time_memo_prof
def doubles_check_2(lst):
    return filter(lambda x: lst.count(x) == 1, lst)


doubles_check_1(num_list)
print(doubles_check_2(num_list))
