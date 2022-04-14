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
import string
from collections import deque
from timeit import timeit, default_timer

base_list = [i for i in range(100000)]
lst = base_list
dq = deque(base_list)
my_str = string.ascii_letters

print('Заполнение списка',
      timeit('''for inx in range(1000):
                    lst.append(inx)''', globals=globals(), number=100000))
print('Заполнение дека',
      timeit('''for inx in range(1000):
                    dq.append(inx)''', globals=globals(), number=100000))
print('insert в списке',
      timeit('''for inx in range(1000):
                    lst.insert(0, inx)''', globals=globals(), number=1000))

print('appendleft в деке',
      timeit('''for inx in range(1000):
                    dq.appendleft(inx)''', globals=globals(), number=1000))

print('pop в списке',
      timeit('''for inx in range(1000):
                    lst.pop(0)''', globals=globals(), number=100))
print(len(lst))

print('popleft в деке',
      timeit('''for inx in range(1000):
                    dq.popleft()''', globals=globals(), number=100))
print(len(dq))

base_vol = [1, 2, 3]

print('Заполнение списка',
      timeit('''for inx in range(1000):
                    lst.insert(0, base_vol)''', globals=globals(),
             number=100))
print('Заполнение дека',
      timeit('''for inx in range(1000):
                    dq.extendleft(base_vol)''', globals=globals(),
             number=100))
'''
1. Запонение списка и дека с помощью функции append: 
дека оказалась немного быстрее (5.1913233000000005 против 6.3555935).
2. Заполнение с начала объекта (insert и appendleft): 
дека на порядки быстрее (0.052294899999992595 против 180.4076702).
3. Удаление с начала объекта (pop(0) и popleft:
дека на порядки быстрее (0.005538999999999961 против 1.0139698).
4. Заполнение с начала объекта (insert(0) и extendleft:
дека намного быстрее (0.008901700000000012 против 5.6197057).
'''
