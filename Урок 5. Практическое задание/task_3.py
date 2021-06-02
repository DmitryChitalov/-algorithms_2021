"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
from collections import deque
from timeit import timeit

lis = []
deq = deque()


def create_lst(lis):
    for i in range(10):
        lis.insert(0, i)
        # print(lis)
    return lis


def create_deq(deq):
    for i in range(10):
        deq.appendleft(i)
        # print(deq)


def add_el_list(lis):
    for i in range(100):
        lis.append(i)
        # print(lis)
    return lis


def add_el_deq(deq):
    for i in range(100):
        deq.append(i)
        # print(deq)
    return deq


if __name__ == '__main__':
    print(f'Замер времени выполнения функций при одинаковых значениях параметров:')
    print('*' * 70)
    print(f'Время выполнения функции create_lst:',
          timeit('create_lst([i for i in range(10)])', globals=globals(), number=1000))
    print(f'Время выполнения функции create_deq:',
          timeit('create_deq(deque(i for i in range(10)))', globals=globals(), number=1000))
    print('*' * 70)
    print(f'Время выполнения функции add_el_list:',
          timeit('add_el_list([i for i in range(10)])', globals=globals(), number=1000))
    print(f'Время выполнения функции add_el_deq:',
          timeit('add_el_deq(deque(i for i in range(10)))', globals=globals(), number=1000))


"""
Замер времени выполнения функций при одинаковых значениях параметров:
Результат:
Время выполнения функции create_lst: 0.0010572000000000012 быстрее чем вставка через appendleft
Время выполнения функции create_deq: 0.0011017000000000006 медленнее чем вставка через insert
Время выполнения функции add_el_list: 0.0047782 медленнее чем вставка append deque
Время выполнения функции add_el_deq: 0.0039749 быстрее чем вставка через append list
"""