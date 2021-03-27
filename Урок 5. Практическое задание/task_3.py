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


def func_d_1(test_deque):
    test_deque.append('!')


def func_d_2(test_deque):
    test_deque.appendleft('L')


def func_d_3(test_deque):
    test_deque.index('1')


def func_d_4(test_deque):
    test_deque.reverse()


def func_d_5(test_deque):
    test_deque.count('2')


def func_l_1(test_list):
    test_list.append('!')


def func_l_2(test_list):
    test_list.insert(0, 'L')


def func_l_3(test_list):
    test_list.index('1')


def func_l_4(test_list):
    test_list.reverse()


def func_l_5(test_list):
    test_list.count('2')


testing_deque = deque('123')
testing_list = list('123')
print('Добавление в конец дека: ', timeit("func_d_1(testing_deque)", number=10000, globals=globals()))
print('Добавление в конец списка: ', timeit("func_l_1(testing_list)", number=10000, globals=globals()))
# Список немного медленнее, но разница незначительная

print('Добавление в начало дека: ', timeit("func_d_2(testing_deque)", number=10000, globals=globals()))
print('Добавление в начало списка: ', timeit("func_l_2(testing_list)", number=10000, globals=globals()))
# А в данном случае разнича очень существенная, дек (0.0013) быстрее списка (0.0889)

print('Метод index в деке: ', timeit("func_d_3(testing_deque)", number=10000, globals=globals()))
print('Метод index в списке: ', timeit("func_l_3(testing_list)", number=10000, globals=globals()))
# Взятие по индексу почти идентично, список совсем немного медленнее

print('Разворот дека: ', timeit("func_d_4(testing_deque)", number=10000, globals=globals()))
print('Разворот списка: ', timeit("func_l_4(testing_list)", number=10000, globals=globals()))
# Разворот выполняется значительно быстрее в списке(0.07), чем в деке(0.17)

print('Метод count в деке: ', timeit("func_d_5(testing_deque)", number=10000, globals=globals()))
print('Метод count в списке: ', timeit("func_l_5(testing_list)", number=10000, globals=globals()))
# Этот метод выполняется одинаково медленно для списка и для дека

# Вывод: добавление в начало, разворот (и, конечно, удаление из начала) будут выполняться гораздо быстрее с деком.
# Но нужно учитывать, что при работе с ним нельзя взять срез, что сильно ограничивает.
