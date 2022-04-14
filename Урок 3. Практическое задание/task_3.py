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


Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
"""

import hashlib


def substrings(my_set, in_string):
    for i in range(len(in_string) + 1):
        for j in range(i, len(in_string) + 1):
            substring = in_string[i:j]
            if len(substring) > 0 and len(substring) != len(in_string):
                my_hash = hashlib.sha256(substring.encode('utf-8'))
                my_set.add(my_hash.hexdigest())
    return len(my_set)


string_set = set()
print(substrings(string_set, 'papa'))
