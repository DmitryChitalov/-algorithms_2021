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

test_list = [i for i in range(5000)]
test_deque = deque([i for i in range(5000)])

print('Вставляем в конец list', timeit('test_list.append(5)', globals=globals()))
print('Вставляем в конец deque', timeit('test_deque.append(5)', globals=globals()))
print('Вставляем в начало list', timeit('test_list.insert(0,3)', globals=globals(), number=10000))
print('Вставляем в начало deque', timeit('test_deque.appendleft(3)', globals=globals(), number=10000))
print('Извлекаем из конца list', timeit('test_list.pop()', globals=globals()))
print('Извлекаем из конца deque', timeit('test_deque.pop()', globals=globals()))
print('Извлекаем из начала list', timeit('test_list.pop(0)', globals=globals(), number=10000))
print('Извлекаем из начала deque', timeit('test_deque.popleft()', globals=globals(), number=10000))
print('Расширяем списком в начало list',
      timeit('test_list[:] = [1, 2, 3, 4, 5, 6, 7] + test_list', globals=globals(), number=10000))
print('Расширяем списком в начало deque',
      timeit('test_deque.extendleft([1, 2, 3, 4, 5, 6, 7])', globals=globals(), number=1000))
print('Расширяем спискои в конец list', timeit('test_list.extend([1, 2, 3, 4, 5, 6, 7])', globals=globals()))
print('Расширяем списком в конец deque', timeit('test_deque.extend([1, 2, 3, 4, 5, 6, 7])', globals=globals()))
print('Выбераем случайное число внутри list', timeit('test_list[randint(0, 99999)]', globals=globals(), number=100000))
print('Выбераем случайное число внутри deque',
      timeit('test_deque[randint(0, 99999)]', globals=globals(), number=100000))
"""
Deque работает быстрее списка во всех случаях вставки и удаления, в разы быстрее если косается вставки или удаления
из начала очереди чем списка, однако доступ к элементам по индексам внутри списка происходит быстрее чем внутри очереди
"""
