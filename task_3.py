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


def create_list():
    lst = [a for a in range(10000)]
    return lst

def operation_list(lst):
    for x in range(1000):
        lst.insert(0, x)



def create_deque():
    dq = deque(a for a in range(10000))
    return dq

def append_deque(dq):
    for a in range(1000):
        dq.appendleft(a)
    #print("append", dq)

def extend_deque(dq):
    for_deque_extend = [a for a in range(1000)]
    dq.extendleft(for_deque_extend)
    #print("extend", dq)

print(
    timeit.timeit(
        "create_list()",
        globals=globals(),
        number=1000), f' - замеры создания словаря')

print(
    timeit.timeit(
        "operation_list(create_list())",
        globals=globals(),
        number=1000), f' - замеры операции добавления в словарь')

print(
    timeit.timeit(
        "create_deque()",
        globals=globals(),
        number=1000), f' - замеры создания deque')

print(
    timeit.timeit(
        "append_deque(create_deque())",
        globals=globals(),
        number=1000), f' - замеры операции appendleft с deque')

print(
    timeit.timeit(
        "extend_deque(create_deque())",
        globals=globals(),
        number=1000), f' - замеры операции extendleft с deque')

"""
0.3685351999956765  - замеры создания словаря
6.931081800001266  - замеры операции добавления в словарь
0.6714375000010477  - замеры создания deque
0.7437607000028947  - замеры операции appendleft с deque
0.7288743000026443  - замеры операции extendleft с deque

"""


"""
deque создается дольше чем list в два раза но время все равно небольшое 
предпочтительнее использовать deque операции с деком так как они имеют сложность O(1)
и в нем проще работать с элементами списки также поддерживают удаление и добавление элементов с начала и конца
но в списках эти операции имеют сложность O(n)
"""

