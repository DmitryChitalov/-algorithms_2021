from collections import deque
from timeit import timeit

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


def my_append(some, value=1):
    return some.append(value)


def my_pop(some):
    return some.pop()


def my_reverse(some):
    return some.reverse()


def my_copy(some):
    return some.copy()


def my_insert(list, value=1):
    list.insert(0, value)


def my_appendleft(deque, value=1):
    deque.appendleft(value)


def my_popleft(deque):
    return deque.popleft()


usr_list = [i for i in range(1000, 10000)]
usr_deque = deque(usr_list)

print(f"my_append(list): {timeit('my_append(usr_list)', globals=globals(), number=10000)} sec.\n"
      f"my_append(deque): {timeit('my_append(usr_deque)', globals=globals(), number=10000)} sec.\n"
      f"my_pop(list): {timeit('my_pop(usr_list)', globals=globals(), number=10000)} sec.\n"
      f"my_pop(deque): {timeit('my_pop(usr_deque)', globals=globals(), number=10000)} sec.\n"
      f"my_reverse(list): {timeit('my_reverse(usr_list)', globals=globals(), number=10000)} sec.\n"
      f"my_reverse(deque): {timeit('my_reverse(usr_deque)', globals=globals(), number=10000)} sec.\n"
      f"my_copy(list): {timeit('my_copy(usr_list)', globals=globals(), number=10000)} sec.\n"
      f"my_copy(deque): {timeit('my_copy(usr_deque)', globals=globals(), number=10000)} sec.\n"
      f"my_insert(list): {timeit('my_insert(usr_list)', globals=globals(), number=10000)} sec.\n"
      f"my_appendleft(deque): {timeit('my_appendleft(usr_deque)', globals=globals(), number=10000)} sec.\n"
      f"my_popleft(deque): {timeit('my_popleft(usr_deque)', globals=globals(), number=10000)} sec.\n")


"""
Функции reverse и copy для deque выполняются медленее, чем для list.
Вставка или получение элементов для Deque выполняются намного быстрее.
Остальные операции выполняются за одинаковое время(приблизительно).
"""
