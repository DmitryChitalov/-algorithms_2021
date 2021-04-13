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

import hashlib


def get_hash(str):
    arr = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            cur_str = str[i:j]
            hash_obj = hashlib.md5(b'cur_str')
            print(str[i:j], hash_obj.hexdigest())
            # hash_obj = hashlib.md5(b'str[i:j]')
            arr.add(hash_obj.hexdigest())

    print('len',len(arr))
    print(arr)


get_hash('papa')
