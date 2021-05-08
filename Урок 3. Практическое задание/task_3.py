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

some_string = 'papa'
uniq_substrings = set()
for i in range(0, len(some_string)+1):
    for j in range(i+1, len(some_string)+1):
        substr = some_string[i:j]
        if substr == some_string:
            continue
        hash_obj = hashlib.sha256(substr.encode('UTF-8'))
        uniq_substrings.add(hash_obj.hexdigest())
print(f'Количество уникальных подстрок в строке "{some_string}" - {len(uniq_substrings)} шт.')

