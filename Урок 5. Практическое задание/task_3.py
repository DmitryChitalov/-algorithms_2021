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
    for i in range(number//2):
        lst.pop(0)


def popleft_deque(number: int):
    for i in range(number//2):
        dq.popleft()


def extandleft_list(arr: list, in_lst: list) -> list:
    in_lst = arr + in_lst

    return in_lst


def extandleft_deque(arr: list):
    dq.extendleft(arr)


if __name__ == '__main__':
    NUMBER = 1000
    SIZE = 1000
    ARR = [23, 34, 45, 56, 67]
    print(f"Execution time of fill_list: "
          f"{timeit('fill_list(SIZE)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of fill_deque: "
          f"{timeit('fill_deque(SIZE)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of appendleft_list: "
          f"{timeit('appendleft_list(SIZE//10)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of appendleft_list_2: "
          f"{timeit('appendleft_list_2(SIZE//10, lst)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of appendleft_deque: "
          f"{timeit('appendleft_deque(SIZE//10)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of popleft_list: "
          f"{timeit('popleft_list(SIZE)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of popleft_deque: "
          f"{timeit('popleft_deque(SIZE)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of extandleft_list: "
          f"{timeit('extandleft_list(ARR, lst)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of extandleft_deque: "
          f"{timeit('extandleft_deque(ARR)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of pop_list: "
          f"{timeit('pop_list()', globals=globals(), number=NUMBER)}")
    print(f"Execution time of pop_deque: "
          f"{timeit('pop_deque()', globals=globals(), number=NUMBER)}")
    print(f"Execution time of extend_list: "
          f"{timeit('extend_list(ARR)', globals=globals(), number=NUMBER)}")
    print(f"Execution time of extend_deque: "
          f"{timeit('extend_deque(ARR)', globals=globals(), number=NUMBER)}")

"""
Execution time of fill_list: 0.055555499999999994
Execution time of fill_deque: 0.044700100000000006
=========================================================
Execution time of appendleft_list: 111.8603032
Execution time of appendleft_list_2: 848.7672498000001
Execution time of appendleft_deque: 0.041238099999986844
=========================================================
Execution time of popleft_list: 323.66882439999995
Execution time of popleft_deque: 0.01934920000007878
=========================================================
Execution time of extandleft_list: 4.676811400000133
Execution time of extandleft_deque: 0.03451039999981731
=========================================================
Execution time of pop_list: 0.026632800000015777
Execution time of pop_deque: 0.02691939999999704
=========================================================
Execution time of extend_list: 0.00022439999997914128
Execution time of extend_deque: 0.0001257999999779713

ВЫВОД:
Все операции с левой (начальной) стороны списка выполняются на порядки медленнее, чем аналогичные операции в деке.
Заполнение дека происходит не сильно быстрее списка, расширение с конца списка почти в два раза медленнее дека, а вот 
операция рор с конца примерно одинакова до тысячных.
"""
