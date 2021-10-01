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

lst = []
dq = deque()


def fill_list(number: int):
    for i in range(number):
        lst.append(i)


def fill_deque(number: int):
    for i in range(number):
        dq.append(i)


def pop_list():
    for i in range(len(lst)//2):
        lst.pop()


def pop_deque():
    for i in range(len(dq)//2):
        dq.pop()


def extend_list(arr: list):
    lst.extend(arr)


def extend_deque(arr: list):
    dq.extend(arr)


def appendleft_list(number: int):
    for i in range(number):
        lst.insert(0, i)


def appendleft_list_2(number: int, in_lst: list) -> list:
    for i in range(number):
        in_lst = [i] + in_lst

    return in_lst


def appendleft_deque(number: int):
    for i in range(number):
        dq.appendleft(i)


def popleft_list(number: int):
    for i in range(number):
        lst.pop(0)


def popleft_deque(number: int):
    for i in range(number):
        dq.popleft()


def extandleft_list(arr: list, in_lst: list) -> list:
    in_lst = arr + in_lst

    return in_lst


def extandleft_deque(arr: list):
    dq.extendleft(arr)


if __name__ == '__main__':
    NUMBER = 10000
    SIZE = 1000
    ARR = [23, 34, 45, 56, 67]
    print(f"Execution time of fill_list: "
          f"{timeit('fill_list(SIZE)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of fill_deque: "
          f"{timeit('fill_deque(SIZE)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of pop_list: "
          f"{timeit('pop_list()', globals=globals(), number=NUMBER)}")
    print(f"Execution time of pop_deque: "
          f"{timeit('pop_deque()', globals=globals(), number=NUMBER)}")
    print(f"Execution time of extend_list: "
          f"{timeit('extend_list(ARR)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of extend_deque: "
          f"{timeit('extend_deque(ARR)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of appendleft_list: "
          f"{timeit('lst = appendleft_list(SIZE//10)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of appendleft_list_2: "
          f"{timeit('lst = appendleft_list_2(SIZE//10, lst)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of appendleft_deque: "
          f"{timeit('appendleft_deque(SIZE//10)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of popleft_list: "
          f"{timeit('popleft_list(SIZE)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of popleft_deque: "
          f"{timeit('popleft_deque(SIZE)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of extandleft_list: "
          f"{timeit('lst = extandleft_list(ARR, lst)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of extandleft_deque: "
          f"{timeit('extandleft_deque(ARR)', globals=globals(), number=NUMBER)}")
