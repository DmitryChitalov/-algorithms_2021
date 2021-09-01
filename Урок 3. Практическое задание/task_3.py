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

from hashlib import sha256

str_s = 'qwerty'
if len(str_s) > 1:
    str_set = set()
    for index in range(len(str_s)):
        for width in range(1, len(str_s) - index + 1):
            sub_str = str_s[index: index + width]
            print(sub_str)
            if sub_str != str_s:
                str_set.add(sha256(sub_str.encode()).hexdigest())
    print(f'{str_s} - {len(str_set)} уникальных подстрок')
