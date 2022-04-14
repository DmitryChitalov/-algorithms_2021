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

my_list_1 = []
my_deque_1 = deque()


def list_append(num):
    for i in range(num):
        my_list_1.append(i)
    return my_list_1


def deque_append(num):
    for i in range(num):
        my_deque_1.append(i)
    return my_deque_1


def list_append_left(num):
    for i in range(num):
        my_list_1.insert(0, i)
    return my_list_1


def deque_append_left(num):
    for i in range(num):
        my_deque_1.appendleft(i)


def list_reverse():
    return my_list_1.reverse()


def deque_reverse():
    return my_deque_1.reverse()


def list_extend():
    return my_list_1.extend(my_list_1)


def deque_extend():
    return my_deque_1.extend(my_deque_1)


print('---------------')
print('Чтобы было наглядно понятно какие операции производятся с my_list_1 и с my_deque_1 представляю:')
list_append(15)
deque_append(15)
print(my_list_1)
print(my_deque_1)
print('---------------')
list_append_left(10)
deque_append_left(10)
print(my_list_1)
print(my_deque_1)
print('---------------')
list_reverse()
deque_reverse()
print(my_list_1)
print(my_deque_1)
print('---------------')
list_extend()
deque_extend()
print(my_list_1)
print(my_deque_1)
print('---------------')
print('А теперь произведём замеры с объектами кратно больше, поэтому выводить тысячи цифр мы не будем,'
      ' а только результаты замеров:')
print('---------------')
print(
    timeit(
        'list_append(100)',
        setup='from __main__ import list_append',
        number=10000))
print(
    timeit(
        'deque_append(100)',
        setup='from __main__ import deque_append',
        number=10000))
print('Здесь мы видим, что deque справляется с задачей заполнения списка быстрее!')
print('---------------')
print(
    timeit(
        'list_append_left(100)',
        setup='from __main__ import list_append_left',
        number=100))
print(
    timeit(
        'deque_append_left(100)',
        setup='from __main__ import deque_append_left',
        number=100))
print('Здесь мы видимо, что deque справляется с задачей append_left в разы, просто многократно лучше!!')
print('---------------')
print(
    timeit(
        'list_reverse()',
        setup='from __main__ import list_reverse',
        number=1000))
print(
    timeit(
        'deque_reverse()',
        setup='from __main__ import deque_reverse',
        number=1000))
print('В случае с функцией reverse мы можем наблюдать, что deque справляется сильно хуже, чем list')
print('---------------')
print(
    timeit(
        'list_extend()',
        setup='from __main__ import list_extend',
        number=3))
print(
    timeit(
        'deque_extend()',
        setup='from __main__ import deque_extend',
        number=3))
print('И в случае с extend мы тоже можем видеть, что deque справляется медленнее')
print('---------------')
