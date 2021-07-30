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
from time import time


def timer(func):
    def temporary(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        delta_time = time() - start_time
        print(f'Время выполнения функции {func.__name__} = {delta_time}')
        return result

    return temporary


new_list = []
new_deque = deque()


@timer
def list_create():  # 0.0050048828125 → Создание списка происходит немного быстрее, чем создание объекта деки.
    global new_list
    new_list = [i for i in range(100000)]


@timer
def deque_create():  # 0.008507490158081055
    global new_deque
    new_deque = deque(i for i in range(100000))


'''Вставка по одному элементу в конец в три раз медленнеее в списке аналогочного действия с декой. 
Вставка одного элемента в начало списка во много раз медленнее аналогичного appendleft деки. 
Appendleft деки по времени почти идентично методу списка append. Самым быстрым способом вставки одного элемента из
перечисленных — append деки.'''


@timer
def list_append():  # 0.0015022754669189453
    for i in range(10000):
        new_list.append(i)


@timer
def deque_append():  # 0.0005004405975341797
    for i in range(10000):
        new_deque.append(i)


@timer
def list_insert_0():  # 0.7977581024169922
    for i in range(10000):
        new_list.insert(i, 0)


@timer
def deque_append_left():  # 0.0015017986297607422
    for i in range(10000):
        new_deque.appendleft(i)


@timer
def list_extend():  # 0.004503965377807617 → Медленнее всех способов вставки множетсвенного количества элементов.
    new_list.extend(range(100000))


@timer
def deque_extend():  # 0.004003763198852539 → Быстрее extend списка, но медленне вставки в начало деки.
    new_deque.extend(range(100000))


@timer
def deque_extend_left():  # 0.0035033226013183594 → Самый быстрый способ вставить множественное количество элементов.
    new_deque.extendleft(range(100000))


@timer
def list_pop():  # 0.0015010833740234375 → По скорости pop элемента из списка практически идентично аналогу деки.
    for i in range(10000):
        new_list.pop()


@timer
def deque_pop():  # 0.001501321792602539 → Извлечние элемента из конца деки медленнее извлечнеия из начала деки.
    for i in range(10000):
        new_deque.pop()


@timer
def deque_pop_left():  # 0.0010013580322265625 → Самый быстрый способ извелчения элемента. Единственный из начала.
    for i in range(10000):
        new_deque.popleft()


for j in [list_create(), deque_create(), list_append(), deque_append(), list_insert_0(), deque_append_left(),
          list_extend(), deque_extend(), deque_extend_left(), list_pop(), deque_pop(), deque_pop_left()]:
    j

'''Вывод: работа с декой по скорости является более выигрышной, либо идентичной в сравнение с работой со списками,
 также имеея преимущетсва вариабельности добавления или извлечения элементов в начало или конец.'''