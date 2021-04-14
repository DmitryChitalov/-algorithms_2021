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
from random import randint

list_test = list(range(0, 1000))
deque_test = deque(range(0, 1000))

# append
print("Вставка в конец")
print(f'{timeit("list_test.append(0)", globals=globals(), number=100000)} - list')
print(f'{timeit("deque_test.append(0)", globals=globals(), number=100000)} - deque')

# insert appendleft
print("Вставка в начало")
print(f'{timeit("list_test.insert(0, 0)", globals=globals(), number=100000)} - list')
print(f'{timeit("deque_test.appendleft(0)", globals=globals(), number=100000)} - deque')

# pop
print("Удаление последнего элемента")
print(f'{timeit("list_test.pop()", globals=globals(), number=100000)} - list')
print(f'{timeit("deque_test.pop()", globals=globals(), number=100000)} - deque')

# pop popleft
print("Удаление первого элемента")
print(f'{timeit("list_test.pop(0)", globals=globals(), number=100000)} - list')
print(f'{timeit("deque_test.popleft()", globals=globals(), number=100000)} - deque')

# Доступ к случайному элементу
print("Доступ к случайному элементу")
print(f'{timeit("list_test[randint(0,100)]", globals=globals(), number=100000)} - list')
print(f'{timeit("deque_test[randint(0,100)]", globals=globals(), number=100000)} - deque')

"""
Вставка в конец примерно одинаково
0.014259199999999993 - list
0.013808799999999996 - deque

Вставка в начало deque намного быстрее
10.2411693 - list
0.00929169999999857 - deque

Удаление последнего элемента deque немного быстрее
0.009255600000001252 - list
0.008544000000000551 - deque

Удаление первого элемента deque быстрее
0.8480676000000003 - list
0.013101999999999947 - deque

Доступ к случайному элементу deque немного медленнее
0.17361990000000027 - list
0.18584019999999946 - deque

Вывод:информация в документации верна, при необходимости бысто вытащить или дописать deque работат быстрее,
при необходимости доступа к случайному элементу - list
"""
