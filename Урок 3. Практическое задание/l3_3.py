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


def unique_sub_row(text):

    return len(set([hash(text[i:j]) for i in range(len(text)) for j in range(i + 1, len(text) + 1)]) - {hash(text)})


print(unique_sub_row('papa'))
print(unique_sub_row('abc'))  # → 5: a, ab, b, bc, c
print(unique_sub_row('ab'))  # → 2: a, b
