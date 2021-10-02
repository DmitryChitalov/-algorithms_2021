#!/usr/bin/env python3

from timeit import timeit
from collections import deque

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

l = list()
dq = deque()

number = 100000


def profile_list():
    print(f'#{"-" * 30} LIST {"-" * 30}#')

    print(f"list.append: {timeit('l.append(None)', globals=globals(), number=number)}")
    print(f"list.insert: {timeit('l.insert(0, None)', globals=globals(), number=number)}")
    print(f"list.pop(0): {timeit('l.pop(0)', globals=globals(), number=number)}")
    print(f"list.pop: {timeit('l.pop()', globals=globals(), number=number)}")
    print(f"list.extend: {timeit('l.extend([1,2,3,4,5])', globals=globals(), number=number)}")
    print(f"list[1]: {timeit('l[1]', globals=globals(), number=number)}")
    print(f"list[100]: {timeit('l[100]', globals=globals(), number=number)}")
    print(f"list[1000]: {timeit('l[1000]', globals=globals(), number=number)}")


def profile_deque():
    print(f'#{"-" * 30} DEQUE {"-" * 30}#')

    print(f"deque.append: {timeit('dq.append(None)', globals=globals(), number=number)}")
    print(f"deque.appendLeft: {timeit('dq.appendleft(None)', globals=globals(), number=number)}")
    print(f"deque.popleft: {timeit('dq.popleft()', globals=globals(), number=number)}")
    print(f"deque.pop: {timeit('dq.pop()', globals=globals(), number=number)}")
    print(f"deque.extend: {timeit('dq.extend([1,2,3,4,5])', globals=globals(), number=number)}")
    print(f"deque.extendleft: {timeit('dq.extendleft([1,2,3,4,5])', globals=globals(), number=number)}")
    print(f"deque[1]: {timeit('dq[1]', globals=globals(), number=number)}")
    print(f"deque[100]: {timeit('dq[100]', globals=globals(), number=number)}")
    print(f"deque[1000]: {timeit('dq[1000]', globals=globals(), number=number)}")


def main():
    profile_list()
    profile_deque()


if __name__ == '__main__':
    main()

'''
#------------------------------ LIST ------------------------------#
list.append: 0.009400320996064693
list.insert: 8.342312095002853
list.pop(0): 8.352126874000533
list.pop: 0.007233369993628003
list.extend: 0.01656274301058147
list[1]: 0.003701255001942627
list[100]: 0.004585486996802501
list[1000]: 0.007004305996815674
#------------------------------ DEQUE ------------------------------#
deque.append: 0.009303738988819532
deque.appendLeft: 0.011050439003156498
deque.popleft: 0.008581376998336054
deque.pop: 0.010726942986366339
deque.extend: 0.03159661799145397
deque.extendleft: 0.027221347991144285
deque[1]: 0.0036291319993324578
deque[100]: 0.006622175991651602
deque[1000]: 0.00999463199696038

Работа с "хвостом" у обоих объектов выполняется примерно одинаково
Работа с "головой" у листа значительно медленнее
Произвольный доступ к элементам быстрее у листа, на больших объемах может быть разница может быть существенной

'''
