"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib

def substrings(string):
    substr_set = set()
    for i in range(len(string)):
        for j in range(len(string)):
            substr_set.add(hashlib.sha256(string[i:j].encode()).hexdigest())
    return substr_set

print(len(substrings("aaaaaaa")))

