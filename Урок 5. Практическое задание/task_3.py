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
import timeit

test_deq = deque('qwerty')


def deque_append(el):
    for i in range(el):
        test_deq.append(i)


def deque_apleft(el):
    for i in range(el):
        test_deq.appendleft(i)


def deque_exleft(el):
    for i in range(el):
        test_deq.extendleft([i, f'{i}'])


def deque_popleft(el):
    for _ in range(el):
        test_deq.popleft()


def deque_pop(el):
    for _ in range(el):
        test_deq.pop()


test_list = ['as', 'fd', 'sd']


def list_append(el):
    for i in range(el):
        test_list.append(i)


def list_insert(el):
    for i in range(el):
        test_list.insert(0, i)


def list_extend(el):
    for i in range(el):
        test_list.extend([i, f'{i}'])
    # return test_list


def list_popleft(el):
    for _ in range(el):
        test_list.pop(0)


def list_pop(el):
    for _ in range(el):
        test_list.pop()


function_list = ['deque_append(el)', 'deque_apleft(el)', 'deque_exleft(el)', 'deque_popleft(el)',
                 'deque_pop(el)', 'list_append(el)',  'list_extend(el)', 'list_pop(el)']

el = 100

print(timeit.repeat('list_insert(el)', globals=globals(), number=(10**3)))
print(timeit.repeat('list_popleft(el)', globals=globals(), number=(10**3)))

for i in function_list:
    print(i, min(timeit.repeat(i, globals=globals(), number=(10**5))))

""" Result:
List and deque имеют одинаковую скорость в добавление, удалении конца списка, и разную в тех же операциях
но для начала списка, List медленее в несколько раз по сравнению с deque когда дело касается операция с началом списка
"""