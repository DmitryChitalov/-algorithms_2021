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
from collections import deque
from timeit import timeit
from random import randint

n = 10 ** 4

lst_1 = []
deque_1 = deque()
lst_2 = [i for i in range(10 ** 5)]
deque_2 = deque([i for i in range(10 ** 5)])


def fill_lst(lst):
    for i in range(n):
        lst.insert(0, i)
    return lst


def fill_deque(dq):
    for i in range(n):
        dq.appendleft(i)
    return dq


def change_lst(lst):
    for i in range(90000):
        lst[randint(1, 8001)] = randint(1, 150)
    return lst


def change_deque(dq):
    for i in range(90000):
        dq[randint(1, 8001)] = randint(1, 150)
    return dq


if __name__ == '__main__':
    print('Время заполнения списка при 10 повторениях: ', timeit(
        'fill_lst(lst_1)', setup='from __main__ import fill_lst, lst_1, n', number=10))

    print('Время заполнения двусторонней очереди при 10 повторениях: ', timeit(
        'fill_deque(deque_1)', setup='from __main__ import fill_deque, deque_1, n', number=10))

    print('Время изменения списка при 10 повторениях: ', timeit(
        'change_lst(lst_2)', setup='from __main__ import change_lst, lst_2, n', number=10))

    print('Время изменения двусторонней очереди при 10 повторениях: ', timeit(
        'change_deque(deque_2)', setup='from __main__ import change_deque, deque_2, n', number=10))

#  По результатам замеров чётко видно, что заполнение deque происходит гораздо быстрее, если сравнивать со вставкой
#  каждого элемента в начало списка, связано это с тем, что пересчитываются и все индексы элементов списка,
#  соответственно, сложность операции для deque - O(1), для списка в данном примере - O(n). Операции с изменениями
#  значений в списке выполняются быстрее, но причину этого я не понял, в документации написано, что deque -
#  A list-like sequence optimized for data accesses near its endpoints, может тут в том-то и дело, что deque как раз
#  быстрее отработает "near its endpoints", то есть, если мы меняли бы элементы в начале или конце списка
#  надо будет попробовать то же самое проделать, только ограничить randint индексами в начале и конце списка
#  соответственно
