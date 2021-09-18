"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import deque
from timeit import timeit


def fill_lst():
    lst = []
    for i in range(10000):
        lst.append(i)
    return lst


def fill_deq():
    deq = deque()
    for i in range(10000):
        deq.append(i)
    return deq


print('Заплнение дек/список')
print(timeit('fill_deq()', globals=globals(), number=100))
print(timeit('fill_lst()', globals=globals(), number=100))


ex_list = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
l1 = fill_lst()
d1 = fill_deq()


def ap_l_deq(deq):
    """Добавление элемента в начало дека(слева)"""
    deq.appendleft(9999)
    return deq


def pop_l_deq(deq):
    """Удаление элемента дека слева"""
    el = deq.popleft()
    return el


def ex_l_deq(deq, iterable):
    """Расширяет дек с левой стоорны за счет элементов итерируемого объекта"""
    new_deq = deq.extendleft(iterable)
    return new_deq


def ap_deq(deq):
    """Добавление элемента с правой стороны дека"""
    deq.append(1000)
    return deq


def ins_list(lst):
    """Добавление элемента в начало списка"""
    lst.insert(0, 9999)
    return lst


def pop0_lst(lst):
    """Удаление первого [0] элемента списка"""
    el = lst.pop(0)
    return el


def ex_lst(lst):
    """Добавление элементов другого списка в начало данного списка"""
    for i in ex_list:
        lst.insert(0, i)
    return lst


def ap_lst(lst):
    """Добавление элемента в конкц списка"""
    lst.append(1000)
    return lst


print('Добавление в начало (дек, список)')
print(timeit('ap_l_deq(d1)', globals=globals(), number=1000))
print(timeit('ins_list(l1)', globals=globals(), number=1000))

print('Удаление первого(левого) элемента (дек, список)')
print(timeit('pop_l_deq(d1)', globals=globals(), number=10000))
print(timeit('pop0_lst(l1)', globals=globals(), number=10000))

print('Наращивание сначала(слева) (дек, список)')
print(timeit('ex_l_deq(d1, ex_list)', globals=globals(), number=1000))
print(timeit('ex_lst(l1)', globals=globals(), number=1000))

print('Добавление элемента(справа) (дек, список)')
print(timeit('ap_deq(d1)', globals=globals(), number=10000))
print(timeit('ap_lst(l1)', globals=globals(), number=10000))
