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

MY_STR = 'apap'
if len(MY_STR) > 1:
    sub_str_set = set()
    for idx in range(len(MY_STR)):
        for width in range(1, len(MY_STR) - idx + 1):
            sub_str = MY_STR[idx: idx + width]
            if sub_str != MY_STR:
                sub_str_set.add(hashlib.sha256(sub_str.encode()).hexdigest())
    print(f'{MY_STR} - {len(sub_str_set)} уникальных подстрок')
