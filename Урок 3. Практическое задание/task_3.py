"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import time


def timer_for_func(func):
   def timer(*args, **kwargs):
       start_val = time.time()
       result = func(*args, **kwargs)
       end_val = time.time()
       return result, end_val-start_val
   return timer


@timer_for_func
def find_uniq_substr_by_set(my_str, is_print=False):
    my_set = set()
    for i in range(len(my_str)):
        for j in range(i+1, len(my_str)+1):
            sub_str = my_str[i:j]

            hash_str = hash(sub_str)

            if hash_str not in my_set and sub_str != my_str:
                my_set.add(hash_str)
                if is_print:
                    print(sub_str)
    return len(my_set)


@timer_for_func
def find_uniq_substr_by_dict(my_str, is_print=False):
    my_dict = {}
    for i in range(len(my_str)):
        for j in range(i+1, len(my_str)+1):
            sub_str = my_str[i:j]

            if my_dict.get(sub_str) == None and sub_str != my_str:
                my_dict[sub_str] = 0
                if is_print:
                    print(sub_str)
    return len(my_dict)

my_str = 'papa'
print('Для предлагаемой строки "papa", всего {0[0]} уникальных подстрок (через ХЭШ и множество)'.format(list(find_uniq_substr_by_set(my_str, True))))

my_str = input('Введите другую строку (желательно длинную, для сравнения вариантов расчета): ')

print('Всего {0[0]} уникальных подстрок (через ХЭШ и множество), время: {0[1]}'.format(list(find_uniq_substr_by_set(my_str))))
print('Всего {0[0]} уникальных подстрок (черех ХЭШируемые ключи словаря), время: {0[1]}'.format(find_uniq_substr_by_dict(my_str)))
