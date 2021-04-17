"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

# Полезная документация:
# https://docs.python.org/3/library/collections.html#collections.deque

from timeit import repeat, default_timer

deque_import_code = "from collections import deque"

list_create_code = "l = list('BCDEFGHIJKLMNOPQRSTUVWXY')"
deque_create_code = "d = deque('BCDEFGHIJKLMNOPQRSTUVWXY')"


def get_list_create_code(length=pow(10, 4)):
    return f'l = [item for item in range({length})]'


def get_deque_create_code(length=pow(10, 4)):
    return f'd = deque([item for item in range({length})])'


list_setup = list_create_code
deque_setup = f'{deque_import_code}\n{deque_create_code}'


def get_list_setup(length):
    return get_list_create_code(length)


def get_deque_setup(length):
    return f'{deque_import_code}\n{get_deque_create_code(length)}'


repeat_number = pow(10, 5)
print(f'1. make a new deque {repeat_number} times')

print('list')
# [0.041611552999999996, 0.035245307000000003, 0.03590511099999999]
print(repeat(list_create_code, "", default_timer, 3, repeat_number))
print('deque')
# [0.033508594, 0.033455897999999984, 0.033527002]
print(repeat(deque_create_code, deque_import_code, default_timer, 3, pow(10, 5)))

print('deque')
# [0.03745678700000002, 0.04363481300000005, 0.04225130300000002]
print(repeat(deque_create_code, deque_import_code, default_timer, 3, pow(10, 5)))
print('list')
# [0.03636483699999998, 0.03447713200000002, 0.035460424000000046]
print(repeat(list_create_code, "", default_timer, 3, pow(10, 5)))

# создание списка и deque из строки занимает примерно одинаковое время
# времени занимает больше почему то тот, который идет первым при замерах
# deque == list

repeat_number = pow(10, 5)
print(f'2. add a new entry to the right side {repeat_number} times')

print('list')
# [0.004675100000000043, 0.005542799999999959, 0.0035315000000000207]
print(repeat("l.append('Z')", list_setup, default_timer, 3, repeat_number))
print('deque')
# [0.0038878999999999997, 0.003785700000000003, 0.0039619999999999655]
print(repeat("d.append('Z')", deque_setup, default_timer, 3, repeat_number))

# Вставка а конец происходит за O(1), так как весь массив не копируется в обоих случаях
# deque == list

repeat_number = pow(10, 4)
print(f'3. add a new entry to the left side {repeat_number} times')

print('list')
# [0.015861100000000017, 0.015681, 0.017432000000000003]
print(repeat("l.insert(0, 'A')", list_setup, default_timer, 3, repeat_number))
print('deque')
# [0.0003665999999999947, 0.0003559000000000201, 0.0003545999999999827]
print(repeat("d.appendleft('A')", deque_setup, default_timer, 3, repeat_number))

# вставка в начало происходит намного быстрее, потому что не просиходит копирование всего массива при вставке вперед
# deque быстрее list

repeat_number = pow(10, 5)
print(f'4. return and remove the rightmost item {repeat_number} times')

print('list')
# [0.004266500000000006, 0.006472900000000004, 0.005029999999999979]
print(repeat("l.pop()", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [0.004106300000000007, 0.005177700000000007, 0.004162099999999946]
print(repeat("d.pop()", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

# удаление последнего элемента в обоих случаях происходит без копирования массива
# deque == list


