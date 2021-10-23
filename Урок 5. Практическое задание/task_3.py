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

import collections
import timeit


def for_deque():
    return collections.deque(i for i in range(500))


def for_list():
    return [i for i in range(500)]


def first_list(my_list):
    my_list.append(55)


def first_deque(my_deque):
    my_deque.append(55)


def second_list(my_list):
    my_list.insert(0, -55)


def second_deque(my_deque):
    my_deque.appendleft(-55)


def third_list(my_list):
    my_list.pop(0)


def third_deque(my_deque):
    my_deque.popleft()


def fourth_list(my_list):
    my_list[:0] = [0, 5, 6, 8]


def fourth_deque(my_deque):
    my_deque.extendleft([0, 5, 6, 8])


def operations_with_deque(my_deque):
    my_deque.append(55)
    my_deque.appendleft(-55)
    result = my_deque.popleft()
    result += sum(my_deque)
    my_deque.extendleft([0, 5, 6, 8])
    return result


def operations_with_list(my_list):
    my_list.append(55)
    my_list.insert(0, -55)
    result = my_list.pop(0)
    result += sum(my_list)
    my_list[:0] = [0, 5, 6, 8]
    return result


my_deque = for_deque()
my_list = for_list()
operations_with_list(my_list)
operations_with_deque(my_deque)

print('The time of the function "for_deque()" is :',
      timeit.timeit(
          "for_deque()",
          setup='from __main__ import for_deque',
          number=10000), ' secs.')
print('The time of the function "for_list()" is :',
      timeit.timeit(
          "for_list()",
          setup='from __main__ import for_list',
          number=10000), ' secs.')
print('The time of the function "operations_with_deque()" is :',
      timeit.timeit(
          "operations_with_deque(my_deque)",
          setup='from __main__ import operations_with_deque, my_deque',
          number=10000))
print('The time of the function "operations_with_list()" is :',
      timeit.timeit(
          "operations_with_list(my_list)",
          setup='from __main__ import operations_with_list,my_list',
          number=10000))
print('The time of the function "first_list()" is :',
      timeit.timeit(
          "first_list(my_list)",
          setup='from __main__ import first_list,my_list',
          number=10000))
print('The time of the function "first_deque()" is :',
      timeit.timeit(
          "first_deque(my_deque)",
          setup='from __main__ import first_deque,my_deque',
          number=10000))
print('The time of the function "second_list()" is :',
      timeit.timeit(
          "second_list(my_list)",
          setup='from __main__ import second_list,my_list',
          number=10000))
print('The time of the function "second_deque()" is :',
      timeit.timeit(
          "second_deque(my_deque)",
          setup='from __main__ import second_deque,my_deque',
          number=10000))
print('The time of the function "third_list()" is :',
      timeit.timeit(
          "third_list(my_list)",
          setup='from __main__ import third_list,my_list',
          number=10000))
print('The time of the function "third_deque()" is :',
      timeit.timeit(
          "third_deque(my_deque)",
          setup='from __main__ import third_deque,my_deque',
          number=10000))
print('The time of the function "fourth_list()" is :',
      timeit.timeit(
          "fourth_list(my_list)",
          setup='from __main__ import fourth_list,my_list',
          number=10000))
print('The time of the function "fourth_deque()" is :',
      timeit.timeit(
          "fourth_deque(my_deque)",
          setup='from __main__ import fourth_deque,my_deque',
          number=10000))

# создании список и дэка у меня получаются приблизительны,но операции с дэками на +- 5% быстрее, по одельности
# функции с дэками работают быстрее, кроме вставка в конец.
