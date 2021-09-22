import random
from functools import reduce

"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

rand_list = [random.randint(0, 200) for el in range(int(input('Please enter the number of list`s elements: ')))]
print(rand_list)


# def min_num(rnd_lst):
#     min_n = rnd_lst[-1]
#     for i in rnd_lst:
#         if i < min_n:
#             min_n = i
#     return min_n
# # O(n)


# def m_num_rnd_num():
#     rnd_list = [random.randint(0, 200) for el in range(10)]
#     print(rnd_list)
#     rnd_list.sort()
#     mn_num = rnd_list[0]
#     return mn_num
# # O(n log n)


def min_list_el(rnd_lst):
    return reduce(lambda x, y: x if x < y else y, rnd_lst)


# O(n)


# def m_l_e(rnd_lst, min_=None):
#     if min_ is None:
#         min_ = rnd_lst.pop()
#     current = rnd_lst.pop()
#     if current < min_:
#         min_ = current
#     if rnd_lst:
#         return m_l_e(rnd_lst, min_)
#     return min_
# # O(n)


def l_min_n(rnd_lst):
    for el in rnd_lst:
        _min = True
        for num in rnd_lst:
            if el > num:
                _min = False
        if _min:
            return el


# O(n*2)


# print(min_num(rand_list))
# print(m_num_rnd_num())
print(min_list_el(rand_list))
# print(m_l_e(rand_list))
print(l_min_n(rand_list))

# Тут несколько вариантов с О(n), а вот с О(n*2) что-то не выходит придумать еще