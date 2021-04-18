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

print()

# создание списка и deque из строки занимает примерно одинаковое время
# времени занимает больше почему то тот, который идет первым при замерах
# deque == list

repeat_number = pow(10, 5)
print(f'2. append. add a new entry to the right side {repeat_number} times')

print('list')
# [0.004675100000000043, 0.005542799999999959, 0.0035315000000000207]
print(repeat("l.append('Z')", list_setup, default_timer, 3, repeat_number))
print('deque')
# [0.0038878999999999997, 0.003785700000000003, 0.0039619999999999655]
print(repeat("d.append('Z')", deque_setup, default_timer, 3, repeat_number))

print()

# Вставка а конец происходит за O(1), так как весь массив не копируется в обоих случаях
# deque == list

repeat_number = pow(10, 4)
print(f'3. appendleft. add a new entry to the left side {repeat_number} times')

print('list')
# [0.015861100000000017, 0.015681, 0.017432000000000003]
print(repeat("l.insert(0, 'A')", list_setup, default_timer, 3, repeat_number))
print('deque')
# [0.0003665999999999947, 0.0003559000000000201, 0.0003545999999999827]
print(repeat("d.appendleft('A')", deque_setup, default_timer, 3, repeat_number))

print()

# вставка в начало происходит намного быстрее, потому что не просиходит копирование всего массива при вставке вперед
# deque быстрее list

repeat_number = pow(10, 5)
print(f'4. pop. return and remove the rightmost item {repeat_number} times')

print('list')
# [0.004266500000000006, 0.006472900000000004, 0.005029999999999979]
print(repeat("l.pop()", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [0.004106300000000007, 0.005177700000000007, 0.004162099999999946]
print(repeat("d.pop()", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

print()

# удаление последнего элемента в обоих случаях происходит без копирования массива
# deque == list

repeat_number = pow(10, 3)
print(f'5. popleft. return and remove the leftmost item {repeat_number} times')

print('list')
# [0.0010859999999999759, 0.0010796000000000139, 0.0010776000000000119]
print(repeat("l.pop(0)", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [4.16000000000305e-05, 3.819999999998824e-05, 3.739999999996524e-05]
print(repeat("d.popleft()", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

print()

# удаление первого элемента в deque происходит за O(1), в то время, как в list за O(n)
# deque быстрее list

repeat_number = pow(10, 5)
print(f'6. [0]. peek at leftmost item {repeat_number} times')

print('list')
# [0.0027522999999999853, 0.0021387999999999963, 0.0021711999999999843]
print(repeat("l[0]", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [0.003248099999999976, 0.0024935999999999847, 0.005839299999999992]
print(repeat("d[0]", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

print()

# взятие самого левого элемента в обоих случаях происходоит за O(1)
# deque == list

repeat_number = pow(10, 5)
print(f'7. [-1]. peek at rightmost item {repeat_number} times')

print('list')
# [0.0022420999999999136, 0.0021839000000000164, 0.002968900000000052]
print(repeat("l[-1]", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [0.002835299999999985, 0.002761700000000089, 0.002831499999999987]
print(repeat("d[-1]", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

print()

# deque == list

repeat_number = pow(10, 4)
print(f'8. reversed. list the contents of a deque in reverse {repeat_number} times')

print('list')
# [0.0009265999999999996, 0.001266999999999907, 0.0013853000000000337]
print(repeat("reversed(l)", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [0.0009896999999999823, 0.0008452999999999378, 0.001848599999999978]
print(repeat("reversed(d)", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

print()

# deque == list

repeat_number = pow(10, 3)
print(f'9. "el" in. search the deque {repeat_number} times')

print('list')
# [0.012799499999999964, 0.01284390000000002, 0.014558599999999977]
print(repeat("'50' in l", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [0.0146482, 0.013597999999999999, 0.01420330000000003]
print(repeat("'50' in d", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

print()

# deque == list

repeat_number = pow(10, 5)
print(f'10. extend. add multiple elements at once {repeat_number} times')

print('list')
# [0.014948699999999926, 0.015719499999999997, 0.0170207]
print(repeat("l.extend('jkl')", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [0.008650799999999959, 0.0077696999999999905, 0.00844250000000002]
print(repeat("d.extend('jkl')", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

print()

# deque == list

repeat_number = pow(10, 4)
print(f'11. rotate(1). right rotation {repeat_number} times')

print('list')
# [0.39276579999999994, 0.5079151000000002, 0.49243270000000017]
print(repeat("l[1:] + l[:1]", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [0.0005961999999999357, 0.0005996000000001445, 0.0005901999999999852]
print(repeat("d.rotate(1)", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

print()

# для того, чтобы в list сделать rotate нескольких элементов нужно копировать весь массив 2 раза, в то время,
# как в deque перемещнеие нужно делать только n раз, где n - количество перемещаемых элементов
# deque быстрее list

repeat_number = pow(10, 4)
print(f'12. rotate(-1). left rotation {repeat_number} times')

print('list')
# [0.5052783999999999, 0.5051160000000001, 0.5118465000000003]
print(repeat("l[-1:] + l[:-1]", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [0.0006184000000000189, 0.0006186000000001357, 0.000617899999999949]
print(repeat("d.rotate(-1) ", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

print()

# для того, чтобы в list сделать rotate нескольких элементов нужно копировать весь массив 2 раза, в то время,
# как в deque перемещнеие нужно делать только n раз, где n - количество перемещаемых элементов
# deque быстрее list

repeat_number = pow(10, 4)
print(f'13. extendleft. extendleft() reverses the input order {repeat_number} times')

print('list')
# [0.20890559999999958, 0.21956069999999972, 0.19527819999999974]
print(repeat("list('abc') + l", get_list_setup(repeat_number), default_timer, 3, repeat_number))
print('deque')
# [0.0008381000000001748, 0.0008685000000001608, 0.0008266999999992919]
print(repeat("d.extendleft('abc')", get_deque_setup(repeat_number), default_timer, 3, repeat_number))

print()

# для того, чтобы в list вставить несколько элементов в начале нужно переписать весь исходный список,
# в deque нужно лишь 3 раза добавить вначало
# deque быстрее list
