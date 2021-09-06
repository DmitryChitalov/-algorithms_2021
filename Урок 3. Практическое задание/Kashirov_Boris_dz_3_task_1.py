"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""


import time
import random


def my_timer(callback):
    """Функция секундомер, для подсказки"""
    def my_tmp(*args, **kwargs):
        start = time.perf_counter_ns()
        res = callback(*args, **kwargs)
        print("Время выполнения", {callback}, f'{(time.perf_counter_ns() - start)/(10**6):.03f}', 'мс')
        return res
    return my_tmp


my_list = []
my_dict = {}
value_str = 'abcdefghijklmnopqrstuvwxyz' * 10**3


# заполнение списка и словаря программно
@my_timer
def my_list_convert(new_lst, values):  # O(1)
    for i in range(len(values)):
        new_lst.append(values[i:i+1])
    return new_lst


@my_timer
def my_dict_convert(new_dict, values):  # O(1)
    for i in range(len(values)):
        new_dict[i] = values[i:i+1]
    return new_dict


my_list_convert(my_list, value_str)
# print(my_list)
# print(len(my_list))
my_dict_convert(my_dict, value_str)
# print(my_dict)

# b) выполните набор операций и со списком, и со словарем


@my_timer
def my_list_pop(old_list, i=0):
    while i < len(old_list)-10:
        old_list.pop()
        i += 1
    return old_list


@my_timer
def my_list_pop_2(old_list):
    while len(old_list) > 0:
        i = random.randint(0, len(old_list) - 1)
        old_list.pop(i)
    # for i in range(len(old_list)-1):
    #     old_list.pop()


@my_timer
def my_dict_pop(old_dict, i=0):
    while i < len(old_dict)-10:
        old_dict.popitem()
        i += 1
    return old_dict


@my_timer
def my_dict_pop_2(old_dict):
    while len(old_dict) > 1:
        nums = list(range(len(old_dict)-1))
        random.shuffle(nums)
        # i = random.randint(0, len(old_dict)-1)
        # if old_dict.get(i):
        for i in nums:
            old_dict.pop(i)


my_list_pop(my_list.copy())
# print(my_list)
my_list_pop_2(my_list.copy())

# my_dict.pop()

my_dict_pop(my_dict.copy())
# print(len(my_dict))
my_dict_2 = my_dict.copy()
# my_last_var = my_dict_pop_2(my_dict_2)
my_dict_pop_2(my_dict_2)

# Результат запуска:
# Время выполнения {<function my_list_convert at 0x000001333B85AF70>} 6.803 мс
# Время выполнения {<function my_dict_convert at 0x000001333B8450D0>} 7.179 мс
# Время выполнения {<function my_list_pop at 0x000001333B8451F0>} 5.162 мс
# Время выполнения {<function my_list_pop_2 at 0x000001333B845310>} 241.886 мс
# Время выполнения {<function my_dict_pop at 0x000001333B845430>} 4.259 мс
# Время выполнения {<function my_dict_pop_2 at 0x000001333B845550>} 28.913 мс

# Вывод: список последовательно заполняется немного быстрее, так как ему не надо присваивать ключ для значения.
# Но при этом операции по индексу (или ключу) для спска выполняются гораздо медленее,
# так как словарь - это хеш-таблица
