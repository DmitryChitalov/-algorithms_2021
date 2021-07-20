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


from hashlib import sha256

my_set = set()


def unique_count(string):
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i:j+1] != string and string[i:j+1] != '':
                my_set.add(sha256(string[i:j+1].encode()).hexdigest())
    print(my_set)
    return my_set


print(f'Кол-во уникальных подстрок: {len(unique_count("papa"))}')