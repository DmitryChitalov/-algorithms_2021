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
import random
from collections import deque
from timeit import timeit


def get_time(func_lst):
    for el in func_lst:
        print(f'Выремя выполнения функции {el}: {timeit(el, globals=globals(), number=10000)}')


data_lst = [el for el in range(1000)]
data_deque = deque(el for el in range(1000))


def append_lst():
    for el in range(100):
        data_lst.append(-el)


def append_deque():
    for el in range(100):
        data_deque.append(-el)


def appendleft_deque():
    for el in range(100):
        data_deque.appendleft(-(el + 100))


def appendleft_lst():
    for el in range(100):
        data_lst.insert(0, -(el + 100))


def popleft_deque():
    for el in range(100):
        data_deque.popleft()


def popleft_lst():
    for el in range(100):
        data_lst.pop(0)


def extendleft_deque():
    data_deque.extendleft(-(el + 200) for el in range(100))


def extend_lst():
    data_lst.extend((-(el + 200) for el in range(100)))


def in_lst():
    matem = [random.randint(0, 1000) for el in range(100)]
    result = [el for el in data_lst if el in matem]
    return result


def in_deque():
    matem = deque(random.randint(0, 1000) for el in range(100))
    result = deque(el for el in data_lst if el in matem)
    return result


str_for_timeit = ['data_lst', 'data_deque', 'append_lst()', 'append_deque()', 'appendleft_deque()', 'appendleft_lst()',
                  'popleft_deque()', 'popleft_lst()', 'extendleft_deque()', 'extend_lst()', 'in_lst()', 'in_deque()']


get_time(str_for_timeit)

"""
Значения времени выполнения:
Выремя выполнения функции data_lst: 0.00012539999999999774
Выремя выполнения функции data_deque: 0.00012459999999999555
Выремя выполнения функции append_lst(): 0.0605853
Выремя выполнения функции append_deque(): 0.052233299999999996
Выремя выполнения функции appendleft_deque(): 0.0664565
Выремя выполнения функции appendleft_lst(): 1427.0585174
Выремя выполнения функции popleft_deque(): 0.04472950000013043
Выремя выполнения функции popleft_lst(): 1026.9583565
Выремя выполнения функции extendleft_deque(): 0.07281530000000203
Выремя выполнения функции extend_lst(): 0.07701689999976224

На последние 2е функции установил число итераций 1000.
Выремя выполнения функции in_lst(): 0.8401099
Выремя выполнения функции in_deque(): 0.8354997


Время выполнения устойчиво демонстрирует преимущество deque перед обычным списком. 
Очень ощутимым это преимущество становится когда нужно работать с началом списка - разница во времени не сопоставима!
appendleft_deque(): 0.0664565 против appendleft_lst(): 1427.0585174.

Вывод: в связи с тем, что функционал один и тот же, лучше использовать deque.
"""