from decor import decor
from recordclass import recordclass
from numpy import array

"""
Задачи из Алгоритмов и структур
Задача №1 из 3 урока
Реализуйте свои пользовательские функции, в которых реализуйте:
выполните набор операций и со списком, и со словарем,
сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему.
"""

# Изначальный вариант

@decor
def inserting_value_1(lst, value):  # O(n) - линейная
    for i in range(value):
        lst.append(i)


@decor
def inserting_value_2(dict, value):  # O(1) - константная
    for i in range(value):
        dict[i] = i


# Оптимизированый вариант

@decor
def inserting_value_3(lst, value):
    lst = array([i for i in range(value)])
    return lst


@decor
def inserting_value_4(dict, value):
    for i in range(value):
        elements = recordclass("var", ["numb_1", "numb_2"])
        dict[elements.numb_1] = elements.numb_2
    return dict


new_list = []
new_dict = {}

inserting_value_1(new_list, 100000)

inserting_value_2(new_dict, 100000)

inserting_value_3(new_list, 100000)

inserting_value_4(new_dict, 100000)

"""
Время работы функции inserting_value_1, составило: 0.01961450 сек.
Выполнение функции inserting_value_1, заняло: 5.1875 Mib.
Время работы функции inserting_value_2, составило: 0.02402670 сек.
Выполнение функции inserting_value_2, заняло: 6.8515625 Mib.
Время работы функции inserting_value_3, составило: 0.03876060 сек.
Выполнение функции inserting_value_3, заняло: 0.7578125 Mib.
Время работы функции inserting_value_4, составило: 24.63674890 сек.
Выполнение функции inserting_value_4, заняло: 0.55859375 Mib.
Выводы по сравнению списка - inserting_value_1, то numpy(array) - inserting_value_3, время выполнения увеличлось в двое,
но зато объем занимаемой памяти уменшился почти в 6 раз.
А по славарю - inserting_value_2 и recordclass - inserting_value_4, время выполнения намного увеличось, но это скорее
реализация заполениния, виновато, но зато объем занимаемой памяти уменшился почти в 13 раз.
"""