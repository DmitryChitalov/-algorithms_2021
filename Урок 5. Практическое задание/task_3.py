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


def append(test, value=1):
    return test.append(value)


def pop(test):
    return test.pop()


def reverse(test):
    return test.reverse()


test_list = [i for i in range(1, 999999)]
test_deque = deque(test_list)

print(f"append(list): {timeit('append(test_list)', globals=globals(), number=10000)} sec.")
print(f"append(deque): {timeit('append(test_deque)', globals=globals(), number=10000)} sec.")
print(f"pop(list): {timeit('pop(test_list)', globals=globals(), number=10000)} sec.")
print(f"pop(deque): {timeit('pop(test_deque)', globals=globals(), number=10000)} sec.")
print(f"reverse(list): {timeit('reverse(test_list)', globals=globals(), number=10000)} sec.")
print(f"reverse(deque): {timeit('reverse(test_deque)', globals=globals(), number=10000)} sec.")

"""
Функции reverse для deque выполняются медленее, чем для простого списка.
Функции append, pop  для deque занчительно быстрее.
"""
