"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
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


"""
При приблизительно одинаковой скорости заполнения дека и списка,
дек выигрывает у списка в скорости операций с элементами , находящимися 
с левой стороны. Опреция с правой стороны, как показал замер, 
приблизительно одинаково затратны.


Заплнение дек/список
0.0627646
0.05609760000000001

Добавление в начало (дек, список)
0.00011559999999999349
0.005827399999999983

Удаление первого(левого) элемента (дек, список)
0.0009659000000000195
0.007286899999999985

Наращивание сначала(слева) (дек, список)
0.00018519999999999648
0.08509420000000001
"""



