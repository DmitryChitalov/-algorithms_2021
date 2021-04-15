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


from collections import deque
from timeit import timeit
from random import randint as rd


def pop_list(ls):
    ls.pop(0)


def pop_deque(deq):
    deq.popleft()


def pop_list_1(ls):
    ls.pop()


def pop_deque_1(deq):
    deq.pop()


def count_list(ls):
    ls.count(5)


def count_deque(deq):
    deq.count(5)


def reverse_list(ls):
    ls.reverse()


def reverse_deque(deq):
    deq.reverse()


def extend_list(ls):
    ls.extend([7, 4, 3, 3])


def extend_deque(deq):
    deq.extend([7, 4, 3, 3])


def extend_deque_1(deq):
    deq.extendleft([7, 4, 3, 3])


def append_list(ls):
    ls.append(7)


def append_deque(deq):
    deq.append(7)


def insert_list(ls):
    ls.insert(0, 7)


def append_left_deque(deq):
    deq.appendleft(7)


def insert_list_mid(ls):
    ls.insert(len(ls) // 2, 7)


def insert_deque_mid(deq):
    deq.insert(len(deq) // 2, 7)


"""
************************* Удаление с начала *************************
list: 0.9340858710000001
deque: 0.008956713000000005
************************* Удаление с конца *************************
list: 0.008191630999999866
deque: 0.008250708000000051
************************* Count  *************************
list: 0.008371778999999968
deque: 0.008846216999999879
************************* Reverse  *************************
list: 0.34363240400000006
deque: 0.597287422
************************* РАСШИРЕНИЕ  *************************
list: 0.002101605999999645
deque: 0.0016464950000001366
deque_2: 0.0016417539999999953
************************* ВСТАВКА В КОНЕЦ *************************
list: 0.0008704729999999827
deque: 0.0008434870000000316
************************* ВСТАВКА В НАЧАЛО *************************
list: 0.08010279400000009
deque: 0.0008485920000000924
************************* ВСТАВКА В СЕРЕДИНУ *************************
list: 0.06879722699999968
deque: 0.09211910700000026

Вывод:
Информация в документации соответствует действительности.
Дэк очень быстро отрабатывает удаление и вставку с НАЧАЛО 
Список показывает себя быстрее в операциях Reverse и вставка в СЕРЕДИНУ
Удаление и вставка в конец/с конца проходи одинаково быстро.
"""


if __name__ == '__main__':
    data_list = [i for i in range(100000)]
    data_deque = deque([el for el in range(100000)])
    print(f'{"*" * 25} Удаление с начала {"*" * 25}')
    print(f'list: {timeit("pop_list(data_list)", globals=globals(), number=100000)}')
    print(f'deque: {timeit("pop_deque(data_deque)", globals=globals(), number=100000)}')
    print(f'{"*" * 25} Удаление с конца {"*" * 25}')
    data_list_1 = [rd(0, 100) for i in range(100000)]
    data_deque_1 = deque([rd(0, 100) for el in range(100000)])
    print(f'list: {timeit("pop_list_1(data_list_1)", globals=globals(), number=100000)}')
    print(f'deque: {timeit("pop_deque_1(data_deque_1)", globals=globals(), number=100000)}')
    print(f'{"*" * 25} Count  {"*" * 25}')
    print(f'list: {timeit("count_list(data_list)", globals=globals(), number=100000)}')
    print(f'deque: {timeit("count_deque(data_deque)", globals=globals(), number=100000)}')
    print(f'{"*" * 25} Reverse  {"*" * 25}')
    data_list_2 = [rd(0, 100) for i in range(100000)]
    data_deque_2 = deque([rd(0, 100) for el in range(100000)])
    print(f'list: {timeit("reverse_list(data_list_2)", globals=globals(), number=10000)}')
    print(f'deque: {timeit("reverse_deque(data_deque_2)", globals=globals(), number=10000)}')
    print(f'{"*" * 25} РАСШИРЕНИЕ  {"*" * 25}')
    data_list_3 = [rd(0, 100) for i in range(100000)]
    data_deque_3 = deque([rd(0, 100) for el in range(100000)])
    print(f'list: {timeit("extend_list(data_list_3)", globals=globals(), number=10000)}')
    print(f'deque: {timeit("extend_deque(data_deque_3)", globals=globals(), number=10000)}')
    print(f'deque_2: {timeit("extend_deque_1(data_deque_3)", globals=globals(), number=10000)}')
    print(f'{"*" * 25} ВСТАВКА В КОНЕЦ {"*" * 25}')
    print(f'list: {timeit("append_list(data_list)", globals=globals(), number=10000)}')
    print(f'deque: {timeit("append_deque(data_deque)", globals=globals(), number=10000)}')
    print(f'{"*" * 25} ВСТАВКА В НАЧАЛО {"*" * 25}')
    print(f'list: {timeit("insert_list(data_list)", globals=globals(), number=10000)}')
    print(f'deque: {timeit("append_left_deque(data_deque)", globals=globals(), number=10000)}')
    print(f'{"*" * 25} ВСТАВКА В СЕРЕДИНУ {"*" * 25}')
    print(f'list: {timeit("insert_list_mid(data_list)", globals=globals(), number=10000)}')
    print(f'deque: {timeit("insert_deque_mid(data_deque)", globals=globals(), number=10000)}')
