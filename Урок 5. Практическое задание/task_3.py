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

from timeit import timeit

"""
Создание дека / списка
"""

print(timeit("""
import collections
my_deque = collections.deque(range(1, 100))
"""))

print(timeit("""
my_list = list(range(1, 100))
"""))

"""
Добавление элемента в конец объекта
"""
print(timeit("""
import collections
my_deque = collections.deque(range(1, 100))
my_deque.append(101)
"""))

print(timeit("""
my_list = list(range(1, 100))
my_list.insert((len(my_list) - 1), 101)
"""))

"""
Удаление элеманта из объекта
"""

print(timeit("""
import collections
my_deque = collections.deque(range(1, 100))
my_deque.pop()
"""))

print(timeit("""
my_list = list(range(1, 100))
my_list.pop()
"""))

"""
Взятие элемента по индексу
"""

print(timeit("""
import collections
my_deque = collections.deque(range(1, 100))
test = my_deque[20]
"""))

print(timeit("""
my_list = list(range(1, 100))
test = my_list[20]
"""))


"""
После проведенных замеров, был немного удивлен результатом. Ожидаось, что как минимум операции
добавления в конец списка у дека будут работать быстрее. Однако, на практике оказалось,
что любые операции, приведенные выше, быстрее выполняются именно со списками. Почему это
так - не совсем ясно.
"""
