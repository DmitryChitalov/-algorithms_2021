"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить,
используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените
что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и
оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft,
extendleft дека и для их аналогов у списков.
"""
from collections import deque
from timeit import timeit


my_list = [i for i in range(10)]
my_deque = deque([i for i in range(10)])
print('Создание списков:')
print('list: ', timeit('my_list = [i for i in range(100)]', globals=globals()))
print('deque: ', timeit('my_deque = deque([i for i in range(100)])',
                        globals=globals()))
print('\nДобавление в начало (по одному)')
print('list:', timeit('my_list.insert(0, 0)', globals=globals(), number=10000))
print('deque: ', timeit('my_deque.appendleft(0)', globals=globals(), number=10000))
print('\nДобавление в конец (по одному)')
print('list:', timeit('my_list.append(0)', globals=globals(), number=10000))
print('deque: ', timeit('my_deque.append(0)', globals=globals(), number=10000))
print('\nУдаление первого элемента:')
print('list:', timeit('my_list.pop(0)', globals=globals(), number=9000))
print('deque: ', timeit('my_deque.popleft()', globals=globals(), number=9000))

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def extend_for_list(list, extend_list): # не нашел встроенной функции списка
    for i in extend_list:
        list.insert(0, i)


print('\nДобавление в начало (iterable)')
print('list:', timeit('extend_for_list(my_list, x)', globals=globals(), number=10000))
print('deque: ', timeit('my_deque.extendleft(x)', globals=globals(), number=10000))

my_list = [i for i in range(100000)]
my_deque = deque([i for i in range(100000)])

print('\nНахождение элемента с индексом 0')
print('list:', timeit('my_list[0] += 1', globals=globals()))
print('deque: ', timeit('my_deque[0] += 1', globals=globals()))
print('\nНахождение элемента с индексом 50000')
print('list:', timeit('my_list[50000] += 1', globals=globals()))
print('deque: ', timeit('my_deque[50000] += 1', globals=globals()))
print('\nНахождение элемента с индексом 99999')
print('list:', timeit('my_list[99999] += 1', globals=globals()))
print('deque: ', timeit('my_deque[99999] += 1', globals=globals()))
print('\nРеверс списков')
print('list:', timeit('my_list.reverse()', globals=globals(), number=10000))
print('deque: ', timeit('my_deque.reverse()', globals=globals(), number=10000))

"""
Исходя из результатов замеров однозначно можно сделать вывод что, 
Если необходима производить операции вида: 
-добавление в начало (по одному или iterable),
-удаление первого элемента.
лучше использовать deque.

Если же необходима работа с индексами во всем списке лучше list 
(чем дальше от краёв в deque, время обработки увеличивается с прогрессией)

Почти на равных:
-нахождение элемента с индексом 0
-Нахождение элемента с индексом последним
-Добавление в конец (по одному)
"""