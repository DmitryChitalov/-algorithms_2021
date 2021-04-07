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

def count_substrings(user_str):
    count_set = set()
    for i in range(len(user_str)):
        for j in range(i + 1, len(user_str) + 1):
            count_set.add(hash(user_str[i:j]))
    return len(count_set) - 1


print(count_substrings('papa'))
