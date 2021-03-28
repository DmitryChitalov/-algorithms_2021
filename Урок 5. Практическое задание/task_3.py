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
from timeit import timeit
from collections import deque


def append_deque(dequels):
    dequels.append(5)


def appendleft_deque(dequels):
    dequels.appendleft(5)


def copy_deque(duquels):
    test = duquels.copy()


def count_deque(duquels):
    duquels.count(5)


def extend_deque(duquels):
    duquels.extend(duquels)


def index_deque(dequels):
    dequels.index(5)


def insert_deque(dequels):
    dequels.insert(5, 5)


def reverse_deque(dequels):
    dequels.reverse()


def get_item_deque(dequels):
    dequels[5]


def append_list(lst):
    lst.append(5)


def insertleft_list(lst):
    lst.insert(5, 0)


def copy_list(lst):
    test = lst.copy()


def count_list(lst):
    lst.count(5)


def extend_list(lst):
    lst.extend(lst)


def index_list(lst):
    lst.index(5)


def insert_list(lst):
    lst.insert(5, 5)


def reverse_list(lst):
    lst.reverse()


def get_item_list(lst):
    lst[5]


val = '123456789'
ls = list(val)
deque_ls = deque(val)

print('deque')
print(timeit('append_deque(deque_ls)', number=1000, globals=globals()))
print(timeit('appendleft_deque(deque_ls)', number=1000, globals=globals()))
print(timeit('copy_deque(deque_ls)', number=10, globals=globals()))
print(timeit('count_deque(deque_ls)', number=1000, globals=globals()))
print(timeit('extend_deque(deque_ls)', number=10, globals=globals()))
print(timeit('index_deque(deque_ls)', number=1000, globals=globals()))
print(timeit('insert_deque(deque_ls)', number=1000, globals=globals()))
print(timeit('reverse_deque(deque_ls)', number=1000, globals=globals()))
print(timeit('get_item_deque(deque_ls)', number=1000, globals=globals()))
print('list')
print(timeit('append_list(ls)', number=1000, globals=globals()))
print(timeit('insertleft_list(ls)', number=1000, globals=globals()))
print(timeit('copy_list(ls)', number=10, globals=globals()))
print(timeit('count_list(ls)', number=1000, globals=globals()))
print(timeit('extend_list(ls)', number=10, globals=globals()))
print(timeit('index_list(ls)', number=1000, globals=globals()))
print(timeit('insert_list(ls)', number=1000, globals=globals()))
print(timeit('reverse_list(ls)', number=1000, globals=globals()))
print(timeit('get_item_list(ls)', number=1000, globals=globals()))
"""
Копирование объекта листа гораздо дольше, чем копирование объекта deque
Инсерт в произвольный индекс листа дольше, чем в deque.
Реверс deque производится дольше, чем list.

На основании замеров, я могу сделать вывод, что deque оптимизирован для добавления и удаления значений из объекта. Это так же подтверждается в нотации big-O
Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.
Список же работает наоборот, к началу и концу big-O стремится к O(n), но к середине O(1)
Считаю, что информация в документации верна.
"""
