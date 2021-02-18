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


def func(some_string):
    hash_list = []
    for i in range(len(some_string) + 1):
        for j in range(i + 1, len(some_string) + 1):
            if hash(some_string[i:j]) not in hash_list and some_string[i:j] != some_string:
                hash_list.append(hash(some_string[i:j]))
    print(len(hash_list))


some_string = 'papa'
func(some_string)
