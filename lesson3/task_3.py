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

# hash?


import hashlib


def count_unique_substrs(input_str):
    substrs_list = []
    for counter in range(1, len(input_str)):
        for i in range(len(input_str)):
            if i + counter <= len(input_str):
                el = input_str[i: i + counter]
                substrs_list.append(el)
            else:
                break

        counter += 1

    print(f'все возможные значения подстрок: {substrs_list}')

input_str = 'papa'
count_unique_substrs(input_str)