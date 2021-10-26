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


def find_sub_str(test_str):
    substrings = set()
    for j in range(1, len(test_str)):
        for i in range(len(test_str)):
            el = test_str[i:i + j]
            el = hash(el.encode())
            substrings.add(el)
    return len(substrings)


print(find_sub_str('papa'))
